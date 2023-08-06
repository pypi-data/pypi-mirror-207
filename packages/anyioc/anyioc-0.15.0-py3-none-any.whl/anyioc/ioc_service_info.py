# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from abc import abstractmethod, ABC
from enum import Enum
from typing import Any
from threading import RLock
import inspect

from .symbols import Symbols
from ._utils import wrap_signature as _wrap_signature


class LifeTime(Enum):
    transient = 0
    scoped = 1
    singleton = 2


class IServiceInfo(ABC):
    __slots__ = ()

    @abstractmethod
    def get(self, provider) -> Any:
        raise NotImplementedError


class ServiceInfo(IServiceInfo):
    '''generic `IServiceInfo`.'''

    __slots__ = (
        '_key', '_lifetime', '_factory', '_factory_origin',
        # for not transient
        '_lock',
        # for singleton
        '_cache_value', '_service_provider',
        # options
        '_options',
    )

    def __init__(self, service_provider, key, factory, lifetime):
        self._factory_origin = factory
        self._factory = _wrap_signature(factory)

        self._key = key
        self._lifetime = lifetime
        self._cache_value = None
        self._service_provider = service_provider
        self._options: dict = service_provider[Symbols.provider_options]

        if self._lifetime != LifeTime.transient:
            self._lock = RLock()
        else:
            self._lock = None

        if self._lifetime == LifeTime.singleton:
            # service_provider is required when lifetime == singleton
            assert self._service_provider is not None

    def __repr__(self) -> str:
        return f'<Service: {self._lifetime}, {self._factory_origin!r}>'

    def get(self, provider):
        if self._lifetime is LifeTime.transient:
            return self._create(provider)

        if self._lifetime is LifeTime.scoped:
            return self._from_scoped(provider)

        if self._lifetime is LifeTime.singleton:
            return self._from_singleton()

        raise NotImplementedError(f'what is {self._lifetime}?')

    def _from_scoped(self, provider):
        cache: dict = provider[Symbols.cache]
        try:
            return cache[self]
        except KeyError:
            pass
        with self._lock:
            try:
                return cache[self]
            except KeyError:
                service = self._create(provider)
                cache[self] = service
                return service

    def _from_singleton(self):
        if self._cache_value is None:
            with self._lock:
                if self._cache_value is None:
                    self._cache_value = (self._create(self._service_provider), )
        return self._cache_value[0]

    def _create(self, provider):
        '''
        return the finally service instance.
        '''

        service = self._factory(provider)
        if self._options['auto_enter']:
            wrapped = getattr(self._factory, '__anyioc_wrapped__', self._factory)
            if isinstance(wrapped, type) and hasattr(wrapped, '__enter__') and hasattr(wrapped, '__exit__'):
                service = provider.enter(service)
        return service


class ProviderServiceInfo(IServiceInfo):
    '''a `IServiceInfo` use for get current `ServiceProvider`.'''

    __slots__ = ()

    def __repr__(self) -> str:
        return '<Provider>'

    def get(self, provider):
        return provider


class GetAttrServiceInfo(IServiceInfo):
    '''getattr from current `ServiceProvider`.'''

    __slots__ = ('_attr_info')

    def __init__(self, *attr_info: tuple):
        super().__init__()
        self._attr_info = attr_info

    def __repr__(self) -> str:
        return f'<GetAttr: {self._attr_info[0]!r}>'

    def get(self, provider):
        return getattr(provider, *self._attr_info)


class ValueServiceInfo(IServiceInfo):
    '''a `IServiceInfo` use for get fixed value.'''

    __slots__ = ('_value')

    def __init__(self, value):
        self._value = value

    def __repr__(self) -> str:
        return f'<Value: {self._value!r}>'

    def get(self, provider):
        return self._value


class GroupedServiceInfo(IServiceInfo):
    '''a `IServiceInfo` use for get multi values as a tuple from keys list.'''

    __slots__ = ('_keys')

    def __init__(self, keys: list):
        self._keys = keys

    def get(self, provider):
        return tuple(provider[k] for k in self._keys)


class BindedServiceInfo(IServiceInfo):
    '''a `IServiceInfo` use for get value from target key.'''

    __slots__ = ('_target_key')

    def __init__(self, target_key):
        self._target_key = target_key

    def __repr__(self) -> str:
        return f'<Binded: {self._target_key!r}>'

    def get(self, provider):
        return provider[self._target_key]


class CallerFrameServiceInfo(IServiceInfo):
    'a `IServiceInfo` use for get caller frameinfo'

    __slots__ = ()

    def get(self, _):
        frs = inspect.getouterframes(inspect.currentframe())
        for fr in frs[2:]:
            mo = inspect.getmodule(fr.frame)
            if mo is None or mo.__name__.partition('.')[0] != 'anyioc':
                return fr
