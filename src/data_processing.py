# src/data_processing.py

import SimpleITK as sitk
import numpy as np
import os
import logging

def load_nifti_file(file_path):
    """
    使用 SimpleITK 读取nii.gz文件并返回图像数据。
    """
    try:
        image = sitk.ReadImage(file_path)
        image_data = sitk.GetArrayFromImage(image)
        return image_data, image
    except Exception as e:
        logging.error(f"加载文件{file_path}时出错：{e}")
        raise
