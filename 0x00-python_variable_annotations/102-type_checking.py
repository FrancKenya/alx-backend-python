#!/usr/bin/env python3
"""
This module provides a type-annotated function
"""

from typing import Sequence, List, Union


def zoom_array(lst: Sequence, factor: Union[int, float] = 2) -> List:
    """
    Zooms into an array by repeating each element `factor` times.

    Args:
        lst (Sequence): The input sequence to zoom into.
        factor (Union[int, float]): The number of
        times to repeat each element.

    Returns:
        List: A zoomed-in list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
