#!/usr/bin/env python3
"""
This module provides a type-annotated function make_multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies
    a float by the multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a
        float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """Multiplies a float by the outer multiplier."""
        return value * multiplier

    return multiplier_function
