#!/usr/bin/env python3
"""
This module provides duck-typed function
"""
from typing import Sequence, TypeVar, Optional

T = TypeVar('T')


def safe_first_element(lst: Sequence[T]) -> Optional[T]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[T]): A sequence of elements.

    Returns:
        Optional[T]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
