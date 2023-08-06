import os

import nibabel as nib
import numpy as np
import pydicom
from easy_mitk import dicom, nifti

from constant import Path
from helper import get_test_tmp_dir


def test_dcm2nii():
    files = os.listdir(Path.DICOM_CASE1)
    test_dir = get_test_tmp_dir(Path.DICOM_CASE1, 'dcm2nii')
    dcm_list = []
    file_list = []
    for name in files:
        file = os.path.join(Path.DICOM_CASE1, name)
        file_list.append(file)
        dcm_list.append(pydicom.dcmread(file))

    nii = dicom.dcm2nii(dcm_list, paths=file_list)

    nii_path1 = os.path.join(test_dir, 'data.nii.gz')
    nib.save(nii, nii_path1),
    nii_path2 = os.path.join(test_dir, 'data.nii')
    nib.save(nii, nii_path2)


def test_sort_slice_by_position():
    dcms = dicom.load_series(Path.DICOM_CASE1)
    result = dicom.sort_slice_by_position(dcms)
    for r in result:
        print(r.ImagePositionPatient)


def test_arr2seg():
    dcms = dicom.load_series(Path.DICOM_CASE1)
    slice_shape = dcms[0].pixel_array.shape
    i, j, k = (*slice_shape, len(dcms))
    mock_mask = np.zeros((i, j, k), dtype=np.uint8)
    
    # mask在column（y）方向尽头结束
    # mask在z方向尽头结束
    mock_mask[i // 4: i * 2 // 4, j // 4: , k // 2: ] = 1          

    seg_obj = dicom.arr2seg(mock_mask, dcms, 'test-seg')
    seg_obj.SeriesDescription = 'Series描述测试'
    pydicom.dcmwrite('tmp/arr2seg.dcm', seg_obj)


def test_dcm2nii():
    target_dir = get_test_tmp_dir(Path.DICOM_CASE1, 'dcm2nii')
    dicom.dcm2nii(Path.DICOM_CASE1, os.path.join(target_dir, 'test.nii.gz'))
    dicom.dcm2nii(Path.DICOM_CASE1, os.path.join(target_dir, 'test.nii'))

def test_dcm2nii2():
    target_dir = get_test_tmp_dir(Path.DICOM_CASE1, 'dcm2nii2')
    series = dicom.load_series(Path.DICOM_CASE1)
    dicom.dcm2nii2(series, save_path=os.path.join(target_dir, 'test.nii.gz'))

def test_seg2arr():
    seg_path = Path.DICOM_SEG3
    # seg_path ='/passer/liver-worker/data/2023/04/26/b3e4534e-d2c4-4718-8d9b-11fa50466cce/tmp/liver.dcm'
    seg = pydicom.dcmread(seg_path)
    seg_arr = dicom.seg2arr(seg)
    print(seg_arr.shape, seg_arr.max(), seg_arr.min(), seg_arr.sum(), np.count_nonzero(seg_arr))
    tmp_path = get_test_tmp_dir(seg_path, 'seg2arr')
    nifti.arr2nii(seg_arr, save_path=os.path.join(tmp_path, 'seg.nii.gz'))
        
    # img_arr = dicom.load_as_arr1(Path.DICOM_CASE1)
    # nifti.arr2nii(img_arr, save_path=os.path.join(tmp_path, 'img.nii.gz'))

def test_seg2nii():
    target_dir = get_test_tmp_dir(Path.DICOM_CASE1_SEG, 'seg2nii')

    origin_img = dicom.load_series(Path.DICOM_CASE1)
    seg = pydicom.dcmread(Path.DICOM_CASE1_SEG)
    nii = dicom.seg2nii(seg, origin_img, save_path=os.path.join(target_dir, 'label.nii.gz'))
    print(nii.affine)


def test_anonymous():
    target_dir = get_test_tmp_dir(Path.DICOM_CASE1, 'anonymous')
    dcms = dicom.load_series(Path.DICOM_CASE1)
    dicom.anonymous(dcms)
    dicom.save_to_disk(dcms, target_dir)

def test_anonymous_dir():
    # dicom.anonymous_dir('test-data/dicom', 'test-data/dicom-anonymous')
    # dicom.anonymous_dir('tmp/quanjing_ct', '/app/sdk/easy-mitk/tmp/quanjing_ct-anonymous')
    dicom.anonymous_dir('tmp/quanjing-mask', 'tmp/quanjing-mask-anonymous')


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    os.chdir(os.path.join(dir, '..'))
    
    test_anonymous_dir()
    # test_anonymous()
    # test_seg2nii()
    # test_dcm2nii2()
