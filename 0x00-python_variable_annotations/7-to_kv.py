#!/usr/bin/env python3
"""
This module provides a type-annotated function to_kv.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int/float.
    Args:
        k (str): The string value.
        v (Union[int, float]): The number to be squared (int or float).

    Returns:
        Tuple[str, float]: A tuple where the first element
        is the string and the second element is the square of the
        number as a float.
    """
    return (k, float(v ** 2))
