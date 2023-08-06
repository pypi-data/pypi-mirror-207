# NOTE: This is an auto-generated file. All modifications will be overwritten.
# type: ignore
from __future__ import annotations

from abc import abstractmethod
from typing import TypeVar, Generic, TypedDict, Optional

from .types import *

from polywrap_core import InvokerClient, UriPackageOrWrapper
from polywrap_plugin import PluginModule
from polywrap_msgpack import GenericMap

TConfig = TypeVar("TConfig")


ArgsGet = TypedDict("ArgsGet", {
    "url": str,
    "request": Optional["Request"]
})

ArgsPost = TypedDict("ArgsPost", {
    "url": str,
    "request": Optional["Request"]
})


class Module(Generic[TConfig], PluginModule[TConfig]):
    def __new__(cls, *args, **kwargs):
        # NOTE: This is used to dynamically add WRAP ABI compatible methods to the class
        instance = super().__new__(cls)
        setattr(instance, "get", instance.get)
        setattr(instance, "post", instance.post)
        return instance

    @abstractmethod
    async def get(
        self,
        args: ArgsGet,
        client: InvokerClient[UriPackageOrWrapper],
        env: None
    ) -> Optional["Response"]:
        pass

    @abstractmethod
    async def post(
        self,
        args: ArgsPost,
        client: InvokerClient[UriPackageOrWrapper],
        env: None
    ) -> Optional["Response"]:
        pass

