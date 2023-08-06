from __future__ import annotations

import contextlib
import datetime
import json
import re
from contextvars import ContextVar
from typing import Type, Dict
from uuid import uuid4

from dotenv import load_dotenv
import logging

from iso8601 import iso8601, ParseError
from pydantic import BaseModel, Field

log = logging.getLogger(__name__)

backend_context_var = ContextVar('backend_context_var')
backend_alias_context_var = ContextVar('backend_alias_context_var', default='default')


def uid():
    return str(uuid4()).replace("-", "")


def utcnow():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)


def str_to_datetime_if_parseable(value: str) -> datetime.datetime | str:
    if len(value) < 8 or value.count('-') != 2:
        return value
    try:
        ret = iso8601.parse_date(value)
    except (ParseError, ValueError, TypeError):
        ret = value
    return ret


class BackendModel(BaseModel):
    uid: str | None = Field(default_factory=uid)
    created_time: datetime.datetime | None = Field(default_factory=utcnow)
    updated_time: datetime.datetime | None = Field(default_factory=utcnow)

    class Config:
        json_encoders = {
            datetime.datetime: lambda x: x.isoformat()
        }
        json_decoders = {
            datetime.datetime: str_to_datetime_if_parseable,
        }


class Backend(object):
    _collections: Dict[Type[BaseModel], str] = {}

    @classmethod
    def startup(cls, alias: str | None = "default"):
        load_dotenv(".env.local")

    @classmethod
    def get_instance(cls, model: Type[BackendModel], uid: str) -> BackendModel:
        raise NotImplementedError()

    @staticmethod
    @contextlib.contextmanager
    def backend_provider(backend: Type[Backend]):
        token = backend_context_var.set(backend)
        yield backend
        backend_context_var.reset(token)

    @staticmethod
    @contextlib.contextmanager
    def alias_provider(alias: str):
        token = backend_alias_context_var.set(alias)
        yield
        backend_alias_context_var.reset(token)

    @staticmethod
    @contextlib.contextmanager
    def alias() -> str:
        yield backend_alias_context_var.get()

    @classmethod
    def collection_name(cls, model: Type[BaseModel]) -> str:
        if model not in cls._collections:
            name = re.sub('([A-Z]+)', r'_\1', model.__name__).lower().removeprefix("_").removesuffix("_model")
            cls._collections[model] = name
        return cls._collections[model]

    @classmethod
    def to_db(cls, instance: BackendModel, json_dict: bool | None = True) -> dict:
        instance.updated_time = utcnow()
        return json.loads(instance.json()) if json_dict else instance.dict()

    @classmethod
    def from_db(cls, model: Type[BackendModel], document: dict, json_dict: bool | None = True) -> BackendModel:
        return model.parse_raw(json.dumps(document)) if json_dict else model.parse_obj(document)


