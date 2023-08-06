import numpy as np
import nibabel as nib


def arr2nii(arr: np.ndarray, affine = np.eye(4), save_path: str = None) -> nib.Nifti1Image:
    """
    Convert array to NIfTI.
    将数组转为NIfTI.

    Args:
        arr (np.ndarray): _description_
        affine (_type_, optional): _description_. Defaults to np.eye(4).
        save_path (str, optional): _description_. Defaults to None.

    Returns:
        nib.Nifti1Image: _description_
    """
    nii = nib.Nifti1Image(arr, affine)
    if save_path:
        nib.save(nii, save_path)
    return nii
