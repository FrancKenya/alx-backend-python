#!/usr/bin/env python3
"""
This module provides a type-annotated function for
calculating the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    A function that returns the floor value of a given float.

    Args:
        n (float): The number to calculate the floor for.

    Returns:
        int: The floor value of the float.
    """
    return math.floor(n)
