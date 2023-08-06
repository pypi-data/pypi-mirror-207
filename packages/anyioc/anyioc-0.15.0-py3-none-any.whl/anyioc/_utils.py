# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
# the internal utils.
# user should not import anything from this file.
# ----------

import sys
import atexit
import inspect

def get_module_name(fr: inspect.FrameInfo):
    'get module name from frame info'
    mo = inspect.getmodule(fr.frame)
    name = '<stdin>' if mo is None else mo.__name__
    return name

def dispose_at_exit(provider):
    '''
    register `provider.__exit__()` into `atexit` module.

    return the `provider` itself.
    '''
    @atexit.register
    def provider_dispose_at_exit():
        provider.__exit__(*sys.exc_info())
    return provider

def update_wrapper(wrapper, wrapped):
    '''
    update wrapper with internal attributes.
    '''
    wrapper.__anyioc_wrapped__ = getattr(wrapped, '__anyioc_wrapped__', wrapped)
    return wrapper

def wrap_signature(func):
    '''
    wrap the function to single argument function.

    unlike the `inject*` series of utils, this is used for implicit convert.
    '''

    sign = inspect.signature(func)
    params = list(sign.parameters.values())
    if len(params) > 1:
        params = [p for p in params if p.kind != inspect.Parameter.VAR_KEYWORD]
    if len(params) > 1:
        params = [p for p in params if p.kind != inspect.Parameter.VAR_POSITIONAL]

    if not params:
        return update_wrapper(lambda _: func(), func)

    elif len(params) == 1:
        arg_0, = params

        if arg_0.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD):
            # does not need to wrap.
            return func

        elif arg_0.kind == inspect.Parameter.KEYWORD_ONLY:
            arg_0_name = arg_0.name
            return update_wrapper(lambda sp: func(**{arg_0_name: sp}), func)

        elif arg_0.kind == inspect.Parameter.VAR_POSITIONAL:
            return update_wrapper(lambda sp: func(sp), func)

        elif arg_0.kind == inspect.Parameter.VAR_KEYWORD:
            return update_wrapper(lambda sp: func(**{'provider': sp}), func)

        else:
            raise ValueError(f'unsupported factory signature: {sign}')

    else:
        raise TypeError('factory has too many parameters.')
