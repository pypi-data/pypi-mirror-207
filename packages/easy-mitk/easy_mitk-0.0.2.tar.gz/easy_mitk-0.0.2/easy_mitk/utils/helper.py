import numpy as np
from typing import Tuple


def bbox(data: np.ndarray) -> Tuple[slice]:
    """
    Compute the max bounding box of a mask.
    返回一个掩膜的最大边框。

    Args:
        data (np.ndarray): _description_

    Returns:
        Tuple[slice]: _description_
    """
    x_min = 0
    while True:
        if np.any(data[x_min, :, :] != 0):
            break
        x_min += 1
    x_max = data.shape[0]
    while True:
        x_max -= 1
        if np.any(data[x_max, :, :] != 0):
            x_max += 1
            break

    y_min = 0
    while True:
        if np.any(data[:, y_min, :] != 0):
            break
        y_min += 1
    y_max = data.shape[1]
    while True:
        y_max -= 1
        if np.any(data[:, y_max, :] != 0):
            y_max += 1
            break
        
    z_min = 0
    while True:
        if np.any(data[:, :, z_min] != 0):
            break
        z_min += 1
    z_max = data.shape[2]
    while True:
        z_max -= 1
        if np.any(data[:, :, z_max] != 0):
            z_max += 1
            break
    # ind = ((100, 300), (100, 300), (30, 90))
    # cropped_data = data[100:300, 100:300, 30:90]
    # ind_ = (slice(*ind[0]), slice(*ind[1]), slice(*ind[2]))
    
    return (slice(x_min, x_max), slice(y_min, y_max), slice(z_min, z_max))
