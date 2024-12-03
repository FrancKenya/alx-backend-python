#!/usr/bin/env python3
"""
This module provides a type-annotated function
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into an array by repeating each element `factor` times.

    Args:
        lst (Tuple): The input tuple to zoom into.
        factor (int): The number of times to repeat each element.

    Returns:
        List: A zoomed-in list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
