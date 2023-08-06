# -*- coding: utf-8 -*-
"""odb_decorators - general decorators for the actions module"""
from functools import wraps
from typing import Callable, Any

def selected(func: Callable) -> Callable:
    @wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        if not args[0]._db:
            return args[0].warning(f'No database selected!')
        else:
            return func(*args, **kwargs)
    return wrapped


def has_table(func: Callable) -> Callable:
    @wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        table_name = args[1].get('table')
        if table_name not in list(args[0]._db.tables(args[0]._mode)):
            return args[0].warning(f'No valid table specified!')
        else:
            return func(*args, **kwargs)
    return wrapped


def has_index(func: Callable) -> Callable:
    @wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        table_name = args[1].get('table')
        index_name = args[1].get('index')
        table = args[0]._db[table_name]
        if index_name not in list(table.indexes()):
            return args[0].warning(f'No valid index specified!')
        else:
            return func(*args, **kwargs)
    return wrapped
