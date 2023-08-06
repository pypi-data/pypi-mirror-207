import os
import vtk
import nibabel as nib
import numpy as np


def volume(nii_path: os.PathLike):
    """
    计算掩膜的体积 (ml)
    Compute volume of the mask (ml).

    Args:
        nii_path (os.PathLike): _description_

    Returns:
        _type_: _description_
    """
    nii: nib.Nifti1Image = nib.load(nii_path)
    pixdim = nii.header['pixdim']
    voxel_size = pixdim[1] * pixdim[2] * pixdim[3]
    arr = nii.get_fdata()
    count = np.count_nonzero(arr)
    return count * voxel_size / 1000

def surface_area(nii_path: os.PathLike):
    """
    计算掩膜的表面积 (cm^2)
    Compute surface area of the mask (cm^2). 

    Args:
        nii_path (os.PathLike): _description_

    Returns:
        _type_: _description_
    """
    assert os.path.exists(nii_path), f'文件不存在: {nii_path}'
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(nii_path)
    reader.Update()

    surface = vtk.vtkContourFilter()
    surface.SetInputData(reader.GetOutput())
    # input_ = surface.GetInput()
    # print(input_.GetPointData().GetScalars())
    # print(surface.GetInputInformation())
    # https://public.kitware.com/pipermail/vtkusers/2009-June/052611.html
    # surface.SetValue(1, 1)  # TODO 这是什么原理，将边界的值设置为1？
    surface.SetValue(0, 1)  # TODO 这是什么原理?
    surface.Update()

    prop = vtk.vtkMassProperties()
    prop.SetInputData(surface.GetOutput())
    prop.Update()
    return prop.GetSurfaceArea() / 100

def surface_area1():
    """TODO 使用ndimage计算
    """
    pass
