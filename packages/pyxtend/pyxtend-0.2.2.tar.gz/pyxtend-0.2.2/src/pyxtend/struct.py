from collections.abc import Iterable
from typing import Any, Union

import numpy as np
from shapely.geometry.base import BaseGeometry


def struct(obj: Any, level: int = 0, limit: int = 3) -> Union[str, dict]:
    """
    Returns the general structure of a given Python object.

    Args:
        obj: The Python object to analyze.
        level: The current depth of recursion (default: 0).
        limit: The maximum number of elements to display for each type (default: 3).

    Returns:
        The structure of the input object as a dictionary or string.
    """
    obj_type_name = type(obj).__name__

    if isinstance(obj, (int, float, bool)):
        return obj_type_name
    elif isinstance(obj, str):
        return "str"
    elif obj_type_name in ["Tensor", "EagerTensor"]:
        return {obj_type_name: [f"{obj.dtype}, shape={tuple(getattr(obj, 'shape', ()))}"]}
    elif isinstance(obj, np.ndarray):
        inner_structure = "empty" if obj.size == 0 else struct(obj.item(0), level + 1)
        return {f"{type(obj).__name__}": [f"{obj.dtype}, shape={obj.shape}"]}
    elif isinstance(obj, BaseGeometry):
        coords = np.array(obj.exterior.coords)
        return {f"{type(obj).__name__}": [f"float64, shape={coords.shape}"]}
    elif isinstance(obj, Iterable) and not isinstance(obj, (str, bytes)):
        if level < limit:
            inner_structure = [struct(x, level + 1) for x in obj]
            if len(obj) > 3:
                inner_structure = inner_structure[:3] + [f"...{len(obj)} total"]
            return {type(obj).__name__: inner_structure}
        else:
            return {type(obj).__name__: "..."}
    else:
        return "unsupported"
