#!/usr/bin/env python3
"""
This module provides a type-annotated function safely_get_value.
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieve the value associated with a key in
    a dictionary-like mapping, or return a default value.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None]): The default value
        to return if the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
