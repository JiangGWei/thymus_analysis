# processing.py

import os
import logging
from src.segmentation import segment_ct_file
from src.data_processing import load_nifti_file
# from src.measurements import (
#     calculate_volume_and_mean_ct,
#     find_largest_volume_slice,
#     find_largest_inscribed_circle,
#     calculate_average_ct_in_circle,
#     calculate_diameters_with_type_check
# )
# from src.visualization import plot_combined_results
from src.utils import load_config, setup_logger, set_environment_variables

def process_ct_file(ct_file_path, config, logger):
    """
    处理单个 CT 文件，执行分割和测量，并返回结果。
    """
    set_environment_variables(config)
    results = {}

    try:
        # 分割输出文件夹
        segmentation_output_folder = config['data']['segmentation_output']
        os.makedirs(segmentation_output_folder, exist_ok=True)

        # 执行分割
        logger.info(f"正在对文件 {ct_file_path} 进行分割...")
        predicted_mask_path = segment_ct_file(ct_file_path, segmentation_output_folder, config)

        if predicted_mask_path is None:
            logger.warning(f"未能生成分割结果。跳过文件 {ct_file_path}")
            return None

        # 加载数据
        ct_data, ct_image = load_nifti_file(ct_file_path)
        mask_data, _ = load_nifti_file(predicted_mask_path)

        # # 计算3D体积和平均CT值
  
        # # 找到体积最大的切片

        #
        # # 找到该切片上的最大内切圆

        #
        # # 计算内切圆中的平均CT值

        #
        # # 计算尺寸和测量指标

        # # 可视化结果


        # # 收集结果

        results = {'文件名': 1}

        logger.info(f"完成文件 {ct_file_path} 的处理。")
        return results
    except Exception as e:
        logger.error(f"处理文件 {ct_file_path} 时出错：{e}")
        return None
