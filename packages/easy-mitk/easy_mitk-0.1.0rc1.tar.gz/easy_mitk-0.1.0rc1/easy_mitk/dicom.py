"""
"""
import os
from datetime import datetime
from glob import glob
from typing import Dict, List, Tuple

import dicom2nifti
import nibabel as nib
import numpy as np
import pydicom
from nibabel import nifti1
from pydicom import Dataset, Sequence, dataset, uid, errors
from rle import encode_pixel_data


def get_slice_location(dcm: Dataset) -> float:
    """
    Get stack position from the SliceLocation.
    :param dcm: DICOM Dataset
    :return:
    """
    return float(dcm.SliceLocation)


def dcm2nii(dcm_dir: os.PathLike, save_path: os.PathLike) -> nifti1.Nifti1Image:
    """
    Convert DICOM image to NIfTI by dicom2nifti.
    使用dicom2nifti将DICOM图像转为NIfTI。

    Args:
        dcm_dir (os.PathLike): _description_
        save_path (os.PathLike): _description_

    Returns:
        nifti1.Nifti1Image: _description_
    """
    # TODO 参考dicom2nifti，但要减少IO
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    nii = dicom2nifti.dicom_series_to_nifti(dcm_dir, save_path)['NII']
    return nii


def dcm2nii2(dcms: List[Dataset], save_path: os.PathLike = None) -> nifti1.Nifti1Image:
    """
    当前只支持水平位扫描方向的图像转换，且不关心图像的方向，只关心图像的内容和像素间距.
    Currently only support scan along the axial direction，and does not care about the direction 
    but the content and the pixel spacing of the image.

    TODO 还是关心一下方向，保证affine计算正确

    Args:
        dcm_list (List[Dataset]): _description_
        save_path (os.PathLike, optional): _description_. Defaults to None.

    Returns:
        nifti1.Nifti1Image: _description_
    """
    assert len(dcms) > 3
    
    affine, arr = get_affine(dcms)
    
    nii = nifti1.Nifti1Image(arr, affine)
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        nib.save(nii, save_path)
    return nii

# 允许与Z轴有10度偏差，cos(80度) = 0.17
SLOPE_TOLERATE = 0.17


def sort_slice_by_position(dcms: List[Dataset]) -> List[Dataset]:
    """
    沿着扫描方向递增。
    Increment in the direction of the scan.

    Args:
        dcms (List[Dataset]): _description_
    """
    assert len(dcms) >= 2, '至少需要两个DICOM文件'
    filtered_dcm = []
    # Remove invalid images
    for dcm in dcms:
        if not hasattr(dcm, 'ImagePositionPatient'):
            continue

        # TODO 暂时只支持水平位切片
        orientation = dcm.ImageOrientationPatient
        # 与z方向几乎垂直即可，90度的余弦值为0
        assert orientation[2] < SLOPE_TOLERATE and orientation[5] < SLOPE_TOLERATE
        filtered_dcm.append(dcm)

    # sort by position
    if len(filtered_dcm) < 1:
        raise Exception('No valid image found')
    filtered_dcm.sort(key=lambda x: x.ImagePositionPatient[2])
    return filtered_dcm


def load_series(dcm_dir: os.PathLike) -> List[Dataset]:
    """
    加载DICOM序列，并根据ImagePositionPatient对每个图像切片进行排序。
    Load DICOM series and sort every image slice by ImagePositionPatient.

    Args:
        dicom_dir (os.PathLike): _description_

    Returns:
        List[Dataset]: _description_
    """
    dcms = []
    for f in glob(f'{dcm_dir}/*'):
        dcms.append(pydicom.dcmread(f))
    return sort_slice_by_position(dcms)


def get_affine(dcms: List[Dataset], load_pixel_arr=True) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute affine matrix from DICOM.
    从DICOM文件计算affine。

    TODO 还是要关心一下方向

    Args:
        dcms (List[Dataset]): _description_
        load_pixel_arr (bool, optional): _description_. Defaults to True.

    Returns:
        Tuple[np.ndarray, np.ndarray]: _description_
    """
    if load_pixel_arr:
        arr = load_as_arr(dcms)
    else:
        arr = None
    d0, d1, d2 = dcms[:3]
    s01 = abs(np.array(d0.ImagePositionPatient) - np.array(d1.ImagePositionPatient))
    s12 = abs(np.array(d1.ImagePositionPatient) - np.array(d2.ImagePositionPatient))
    assert (max(s01) - max(s12)) < 0.001, f'{s01}, {s12}'  # TODO 或者约等于
    z_spacing = max(s01)
    x_spacing, y_spacing = float(d0.PixelSpacing[0]), float(d0.PixelSpacing[1])
    assert x_spacing == y_spacing
    spacing = [x_spacing, y_spacing, z_spacing]
    affine = np.diag(spacing + [0])
    return affine, arr


def load_as_arr(dcms: List[Dataset]) -> np.ndarray:
    """
    Load DICOM series as numpy array.
    将DICOM序列加载为numpy矩阵。

    Args:
        dcms (List[Dataset]): _description_

    Returns:
        np.ndarray: _description_
    """
    arr = []
    for d in dcms:
        # arr.append(np.rot90(d.pixel_array, 1, [0, 1]))
        arr.append(d.pixel_array * d.RescaleSlope + d.RescaleIntercept)
    return np.stack(arr, axis=-1)


def load_as_arr1(dcm_dir: os.PathLike) -> np.ndarray:
    """
    Same with load_as_arr but parameters.
    除了参数，其它与load_as_arr一样。

    Args:
        dcm_dir (os.PathLike): _description_

    Returns:
        np.ndarray: _description_
    """
    dcms = load_series(dcm_dir)
    return load_as_arr(dcms)


def seg2arr(seg: Dataset) -> np.ndarray:
    """
    Convert DICOM SEG to numpy array, and sort by the reference image.
    DICOM SEG转为numpy数组，按照引用图像的顺序排列。

    Args:
        seg (Dataset): _description_
    """
    assert seg.Modality == 'SEG'
    # TODO 保证该SEG文件可以按照以下规则解析

    origin_instances_uid = [i.ReferencedSOPInstanceUID for i in seg.ReferencedSeriesSequence[0].ReferencedInstanceSequence]
    mask = np.zeros((seg.Rows, seg.Columns, len(origin_instances_uid)))

    frames: Sequence[Dataset] = seg.PerFrameFunctionalGroupsSequence
    for i in range(len(frames)):
        frame = frames[i]
        # mask_frame = np.rot90(seg.pixel_array[i], 1, (0, 1))
        mask_frame = seg.pixel_array[i]
        # mask_frame = np.transpose(seg.pixel_array[i], [1, 0])
        ReferenceInstanceUID = frame.DerivationImageSequence[0].SourceImageSequence[0].ReferencedSOPInstanceUID
        segment_number = frame.SegmentIdentificationSequence[0].ReferencedSegmentNumber
        index_ = origin_instances_uid.index(ReferenceInstanceUID)
        mask[:, :, index_][mask_frame==1] = segment_number
    return mask.astype(np.int8)


def arr2seg(arr: np.ndarray, dicom: List[Dataset],
            series_description: str, save_path: os.PathLike = None,
            attributes: dict = {}, segment_label_map = {}) -> Dataset:
    """
    Convert array to DICOM SEG.
    将数组转为DICOM SEG文件。

    Args:
        arr (np.ndarray): _description_
        dicom (List[Dataset]): 原始DICOM图像
        series_description (str): DICOM TAG SeriesDescription
        attributes (Dict): example: {"StudyDescription": "easy_tk_seg"}
        segment_label (Dict): example: {1: 'tumor1', 2: 'tumor2'}

    Returns:
        Dataset: _description_
    """
    assert arr.dtype in [np.int_, np.int8, np.int16, np.int32, np.int64]
    # 依照顺序将arr存入DICOM SEG

    sop_instance_uid = uid.generate_uid(prefix=None)

    meta = dataset.FileMetaDataset()
    # https://dicom.nema.org/medical/dicom/2022b/output/chtml/part10/chapter_7.html
    meta.FileMetaInformationGroupLength = 220
    meta.FileMetaInformationVersion = b'\x00'

    meta.MediaStorageSOPClassUID = uid.SegmentationStorage
    meta.MediaStorageSOPInstanceUID = sop_instance_uid
    meta.TransferSyntaxUID = uid.RLELossless  # ExplicitVRLittleEndian

    # TODO https://dicom.nema.org/medical/dicom/2022b/output/chtml/part07/sect_d.3.3.2.html
    meta.ImplementationClassUID = uid.UID(
        '2.25.80302813137786398554742050926734630921603366648225212145404'
    )
    meta.ImplementationVersionName = 'easy-tk-v0.1'

    d = dataset.FileDataset(save_path, {},
                            file_meta=meta,
                            preamble=b'\0' * 128)
    d.SpecificCharacterSet = 'ISO 2022 IR 58'
    d.is_little_endian = True
    d.is_implicit_VR = False
    d.fix_meta_info()

    # 设置字段
    # series_info = dcm_dataset.ds_series[0]
    series_info = dicom[0]

    d.PatientName = series_info.get('PatientName')
    d.PatientSex = series_info.get('PatientSex')
    d.PatientAge = series_info.get('PatientAge')
    d.PatientID = series_info.get('PatientID')
    d.PatientBirthDate = series_info.get('PatientBirthDate')
    d.PatientWeight = series_info.get('PatientWeight')
    # ds.PatientAddress=self.patientAddress
    d.StudyDate = series_info.get('StudyDate')
    d.StudyID = series_info.get('StudyID')

    StudyDescription: str = series_info.get('StudyDescription')
    if StudyDescription:
        # TODO 先判断一下SpecificCharSet
        b = StudyDescription.encode(encoding='latin1')
        s = b.decode(encoding='GB2312')
        d.StudyDescription = s

    d.Rows = series_info.get('Rows')
    d.Columns = series_info.get('Columns')
    d.BitsAllocated = 8
    d.BitsStored = 8
    d.HighBit = 7
    d.SamplesPerPixel = series_info.get('SamplesPerPixel')
    d.PixelRepresentation = 0
    d.PhotometricInterpretation = series_info.get('PhotometricInterpretation')
    d.FrameOfReferenceUID = series_info.get('FrameOfReferenceUID')
    d.SOPInstanceUID = sop_instance_uid
    d.SOPClassUID = uid.SegmentationStorage  # TODO 是不是和meta重复设置了？
    d.StudyInstanceUID = series_info.get('StudyInstanceUID')
    d.SeriesInstanceUID = pydicom.uid.generate_uid()
    d.SoftwareVersions = '0'
    d.DeviceSerialNumber = '1'
    d.ManufacturerModelName = 'Unspecified'
    d.PositionReferenceIndicator = None
    d.InstanceNumber = 1
    d.AccessionNumber = series_info.get('AccessionNumber')
    d.StudyTime = series_info.get('StudyTime')
    d.LossyImageCompression = '00'
    # additional information
    d.ImageComments = 'Just for research'
    d.ContentDescription = ''
    d.ContentCreatorName = ''
    d.MaximumFractionalValue = 255
    # d.MaximumFractionalValue = 512
    d.SegmentationFractionalType = 'PROBABILITY'
    d.ContentLabel = 'SEGMENTATION'
    d.Modality = 'SEG'
    d.SegmentationType = 'FRACTIONAL'
    d.ContentQualification = 'RESEARCH'
    d.Manufacturer = 'Unspecified'
    d.ImageType = ['DERIVED', 'PRIMARY']
    d.SeriesDescription = series_description
    d.SeriesNumber = 300  # SEG模态的序列号从300开始

    # TODO 和meta.MediaStorageSOPInstanceUID = sop_instance_uid的区别？
    dicom_uid = uid.generate_uid(prefix=None)

    # dim_uid='2.25.196811242094278724812281098897304804485'
    # ReferencedSeriesSequence(RSS)
    ref_series_sequence = Sequence()
    d.ReferencedSeriesSequence = ref_series_sequence
    # Referenced Series Sequence: Referenced Series 1
    ref_series1 = Dataset()

    # Referenced Instance Sequence
    ref_instance_sequence = Sequence()
    for i in range(len(dicom)):
        # 这个需要放到循环里来？？？
        ref_series1.ReferencedInstanceSequence = ref_instance_sequence
        # Referenced Instance Sequence: Referenced Instance 1
        ref_instance1 = Dataset()
        # TODO 使用 MR Image Storage SOP Class?
        # https://dicom.nema.org/medical/dicom/2022b/output/chtml/part02/sect_A.1.html
        ref_instance1.ReferencedSOPClassUID = dicom[i].SOPClassUID
        ref_instance1.ReferencedSOPInstanceUID = dicom[i].SOPInstanceUID
        ref_instance_sequence.append(ref_instance1)

    ref_series1.SeriesInstanceUID = dicom[0].SeriesInstanceUID

    ref_series_sequence.append(ref_series1)

    # Dimension Organization Sequence
    dimension_organization_sequence = Sequence()
    # Dimension Organization Sequence: Dimension Organization 1
    dimension_organization1 = Dataset()
    dimension_organization1.DimensionOrganizationUID = dicom_uid
    dimension_organization_sequence.append(dimension_organization1)
    d.DimensionOrganizationSequence = dimension_organization_sequence

    # Dimension Index Sequence
    dimension_index_sequence = Sequence()
    d.DimensionIndexSequence = dimension_index_sequence
    # Dimension Index Sequence: Dimension Index 1
    dimension_index1 = Dataset()
    dimension_index1.DimensionOrganizationUID = dicom_uid
    dimension_index1.DimensionIndexPointer = (0x0020, 0x9153)
    dimension_index1.FunctionalGroupPointer = (0x0018, 0x9118)
    dimension_index1.DimensionDescriptionLabel = 'ReferencedSegmentNumber'
    dimension_index_sequence.append(dimension_index1)
    # Dimension Index Sequence: Dimension Index 2
    dimension_index2 = Dataset()
    dimension_index2.DimensionOrganizationUID = dicom_uid
    dimension_index2.DimensionIndexPointer = (0x0020, 0x0032)
    dimension_index2.FunctionalGroupPointer = (0x0020, 0x9113)
    dimension_index2.DimensionDescriptionLabel = 'ImagePositionPatient'
    dimension_index_sequence.append(dimension_index2)

    # Segment Sequence
    segment_sequence = Sequence()
    d.SegmentSequence = segment_sequence

    # 标签的数目
    # segment_numbers = set(list(zip(*nifti_information['labelSeries']))[0])
    segment_numbers = np.unique(arr[arr > 0]).tolist()
    for segmentNumber in segment_numbers:
        # Segment Sequence: Segment 1
        segment1 = Dataset()
        # Segmented Property Category Code Sequence
        segmented_property_category_code_sequence = Sequence()
        segment1.SegmentedPropertyCategoryCodeSequence = \
            segmented_property_category_code_sequence
        # Segmented Property Category Code Sequence:
        # Segmented Property Category Code 1
        segmented_property_category_code1 = Dataset()
        segmented_property_category_code1.CodeValue = 'T-D0050'
        segmented_property_category_code1.CodingSchemeDesignator = 'SRT'
        segmented_property_category_code1.CodeMeaning = 'Tissue'
        segmented_property_category_code_sequence.append(
            segmented_property_category_code1)
        segment1.SegmentNumber = segmentNumber
        
        label = segment_label_map.get(int(segmentNumber), f'Tissue{segmentNumber}')
        segment1.SegmentLabel = label
        
        segment1.SegmentAlgorithmType = 'SEMIAUTOMATIC'
        segment1.SegmentAlgorithmName = 'Slicer Prototype'
        segment1.RecommendedDisplayCIELabValue = [34885, 53485, 50171]
        # Segmented Property Type Code Sequence
        segmented_property_type_code_sequence = Sequence()
        segment1.SegmentedPropertyTypeCodeSequence = \
            segmented_property_type_code_sequence
        # Segmented Property Type Code Sequence: Segmented Property Type Code 1
        segmented_property_type_code1 = Dataset()
        segmented_property_type_code1.CodeValue = 'T-D0050'
        segmented_property_type_code1.CodingSchemeDesignator = 'SRT'
        segmented_property_type_code1.CodeMeaning = 'Tissue'
        segmented_property_type_code_sequence.append(
            segmented_property_type_code1)
        segment_sequence.append(segment1)
    # Shared Functional Groups Sequence
    shared_functional_groups_sequence = Sequence()
    d.SharedFunctionalGroupsSequence = shared_functional_groups_sequence
    # Shared Functional Groups Sequence: Shared Functional Groups 1
    shared_functional_groups1 = Dataset()
    # Plane Orientation Sequence
    plane_orientation_sequence = Sequence()
    shared_functional_groups1.PlaneOrientationSequence = \
        plane_orientation_sequence
    plane_orientation1 = Dataset()
    plane_orientation1.ImageOrientationPatient = series_info.get(
        'ImageOrientationPatient')
    plane_orientation_sequence.append(plane_orientation1)
    # Pixel Measures Sequence
    pixel_measures_sequence = Sequence()
    shared_functional_groups1.PixelMeasuresSequence = pixel_measures_sequence
    # Pixel Measures Sequence: Pixel Measures 1
    pixel_measures1 = Dataset()
    pixel_measures1.SliceThickness = series_info.get(
        'SpacingBetweenSlices')  # self.sliceThickness
    pixel_measures1.SpacingBetweenSlices = series_info.get(
        'SpacingBetweenSlices')
    pixel_measures1.PixelSpacing = series_info.get('PixelSpacing')
    pixel_measures_sequence.append(pixel_measures1)
    shared_functional_groups_sequence.append(shared_functional_groups1)
    # Per-frame Functional Groups Sequence
    per_frame_functional_groups_sequence = Sequence()
    d.PerFrameFunctionalGroupsSequence = per_frame_functional_groups_sequence

    frame_values = []
    frame_indexes = []
    for i in range(arr.shape[2]):
        s = arr[:, :, i]
        labels = np.unique(s[s > 0])
        frame_values.extend(labels.tolist())
        # 各个标签的位置，特别注意dtype，一定得是能表示大于原图总张数的类型。
        # 使用np的zero_like, full_like时，生成的数据类型会与参考的矩阵一致（找这个bug花了快4个小时）
        frame_indexes.extend(np.full_like(labels, i, dtype=np.uint32).tolist())

    d.NumberOfFrames = len(frame_indexes)

    # 第一层有2种标签，第二层有3种标签。则总共有5个segment
    for i in range(len(frame_indexes)):
        frame_z = frame_indexes[i]
        frame_value = frame_values[i]
        ref_dicom = dicom[frame_z]
        # Per-frame Functional Groups Sequence: Per-frame Functional Groups 1
        per_frame_functional_groups1 = Dataset()
        # Derivation Image Sequence
        derivation_image_sequence = Sequence()
        per_frame_functional_groups1.DerivationImageSequence = \
            derivation_image_sequence
        # Derivation Image Sequence: Derivation Image 1
        derivation_image1 = Dataset()
        # Source Image Sequence
        source_image_sequence = Sequence()
        derivation_image1.SourceImageSequence = source_image_sequence
        # Source Image Sequence: Source Image 1
        source_image1 = Dataset()
        source_image1.ReferencedSOPClassUID = ref_dicom.SOPClassUID
        # 设置对应frame的原图
        source_image1.ReferencedSOPInstanceUID = ref_dicom.SOPInstanceUID

        # Purpose of Reference Code Sequence
        purpose_of_ref_code_sequence = Sequence()
        source_image1.PurposeOfReferenceCodeSequence = \
            purpose_of_ref_code_sequence
        # Purpose of Reference Code Sequence: Purpose of Reference Code 1
        purpose_of_ref_code1 = Dataset()
        purpose_of_ref_code1.CodeValue = '121322'
        purpose_of_ref_code1.CodingSchemeDesignator = 'DCM'
        purpose_of_ref_code1.CodeMeaning = \
            'Source image for image processing operation'
        purpose_of_ref_code_sequence.append(purpose_of_ref_code1)
        source_image_sequence.append(source_image1)
        # Derivation Code Sequence
        derivation_code_sequence = Sequence()
        derivation_image1.DerivationCodeSequence = derivation_code_sequence
        # Derivation Code Sequence: Derivation Code 1
        derivation_code1 = Dataset()
        derivation_code1.CodeValue = '113076'
        derivation_code1.CodingSchemeDesignator = 'DCM'
        derivation_code1.CodeMeaning = 'Segmentation'
        derivation_code_sequence.append(derivation_code1)
        derivation_image_sequence.append(derivation_image1)
        # Frame Content Sequence
        frame_content_sequence = Sequence()
        per_frame_functional_groups1.FrameContentSequence = \
            frame_content_sequence
        # Frame Content Sequence: Frame Content 1
        frame_content1 = Dataset()

        # frame_content1.DimensionIndexValues = [
        #     # (标签值, 位置)
        #     nifti_information['labelSeries'][frame][0],
        #     nifti_information['labelSeries'][frame][1] + 1
        # ]
        # TODO 为什么要+1
        frame_content1.DimensionIndexValues = [frame_value, frame_z + 1]

        frame_content_sequence.append(frame_content1)
        # Plane Position Sequence
        plane_position_sequence = Sequence()
        per_frame_functional_groups1.PlanePositionSequence = \
            plane_position_sequence
        # Plane Position Sequence: Plane Position 1
        plane_position1 = Dataset()
        position = ref_dicom.ImagePositionPatient
        if not position:
            raise RuntimeError('未能获取到图像的原点坐标')
        plane_position1.ImagePositionPatient = position
        plane_position_sequence.append(plane_position1)
        # Segment Identification Sequence
        segment_identification_sequence = Sequence()
        per_frame_functional_groups1.SegmentIdentificationSequence = \
            segment_identification_sequence
        # Segment Identification Sequence: Segment Identification 1
        segment_identification1 = Dataset()
        segment_identification1.ReferencedSegmentNumber = frame_value
        segment_identification_sequence.append(segment_identification1)
        per_frame_functional_groups_sequence.append(
            per_frame_functional_groups1)
    dt = datetime.now()
    d.ContentDate = dt.strftime('%Y%m%d')
    timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
    d.ContentTime = timeStr
    d.SeriesDate = dt.strftime('%Y%m%d')
    d.SeriesTime = timeStr
    # frames=np.int8(self.framesData).tobytes()
    frames = []
    # # 写入图像数据
    for i in range(len(frame_indexes)):
        frame_value = frame_values[i]
        frame_z = frame_indexes[i]
        slice_ = arr[:, :, frame_z]
        tmp_slice = np.zeros_like(slice_)
        tmp_slice[slice_ == frame_value] = 1
        frame = tmp_slice.astype('uint8')
        frames.append(encode_pixel_data(frame.tobytes(), d))

    print(f'length of frames: {len(frames)}')
    d.PixelData = pydicom.encaps.encapsulate(frames)
    d['PixelData'].is_undefined_length = True
    if save_path:
        pydicom.write_file(save_path, d)
    ds_dir = d.dir()
    for key, value in attributes.items():
        if key in ds_dir:
            setattr(d, key, value)
    return d


def seg2nii(seg: Dataset, origin_dcm: List[Dataset], 
            save_path: os.PathLike=None) -> nib.Nifti1Image:
    """
    Convert DICOM SEG to NIfTI.
    DICOM SEG转为NIfTI.

    Args:
        seg (Dataset): _description_
        origin_dcm (List[Dataset]): _description_
        save_path (os.PathLike, optional): _description_. Defaults to None.

    Returns:
        nib.Nifti1Image: _description_
    """
    arr = seg2arr(seg)
    # spacing = seg.SharedFunctionalGroupsSequence[0].PixelMeasuresSequence[0].PixelSpacing
    # assert spacing[0] == spacing[1]
    referenced_series_uid = seg.ReferencedSeriesSequence[0].SeriesInstanceUID
    assert origin_dcm[0].SeriesInstanceUID == referenced_series_uid
    affine, _ = get_affine(origin_dcm, load_pixel_arr=False)

    nii = nifti1.Nifti1Image(arr, affine)
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        nib.save(nii, save_path)
    return nii


ANONYMOUS_TAGS = {
    "InstitutionName": "", 
    "InstitutionAddress": "",
    "ReferringPhysicianName": "",
    "PatientName": "", 
    "OtherPatientNames": "", 
    "RequestingService": "",
    "StationName": ""
    }

def anonymous(dcms: List[Dataset], anonymous_tags: Dict=ANONYMOUS_TAGS):
    """
    tag: 
    """    
    for d in dcms:
        for k, v in anonymous_tags.items():
            try:
                e = getattr(d, k)
                if isinstance(e, pydicom.DataElement):
                    e: pydicom.DataElement
                    e.value = v
                else:
                    setattr(d, k, v)
            except AttributeError:
                continue
            except Exception as e:
                print(f'failed to set {k} to {v}')
                raise e


def save_to_disk(dcms: List[Dataset], target_dir: os.PathLike):
    os.makedirs(target_dir, exist_ok=True)
    for i in range(len(dcms)):
        full_path = os.path.join(target_dir, f'{i}.dcm')
        pydicom.dcmwrite(full_path, dcms[i])

def anonymous_dir(source_dir: os.PathLike, target_dir: os.PathLike, anonymous_tags: Dict=ANONYMOUS_TAGS):
    assert not str(source_dir).startswith('/'), 'source_dir needs to be a relative path'
    assert os.path.exists(source_dir)
    p = f'{source_dir}/.?*/?*'
    # print(p)
    for root, _, filenames in os.walk(source_dir):
        for i in filenames:
           full_path = os.path.join(root, i)
           print(f'Dealing with: {full_path}')
           try:
               dcm = pydicom.dcmread(full_path)
           except errors.InvalidDicomError:
               # TODO 添加日志文件
               continue
           anonymous([dcm], anonymous_tags)
           target_path = os.path.join(target_dir, full_path)
           os.makedirs(os.path.dirname(target_path), exist_ok=True)
           pydicom.dcmwrite(target_path, dcm)
    # for i in files:
    #     print(i)
