#!/usr/bin/env python3
"""
This module provides a type-annotated function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the result.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all the numbers in the list.
    """
    return sum(input_list)
