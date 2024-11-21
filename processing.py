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
        # thymus_volume, mean_ct_value = calculate_volume_and_mean_ct(ct_data, mask_data, ct_image, target_label=1)
        #
        # # 找到体积最大的切片
        # max_volume_slice_index = find_largest_volume_slice(mask_data, target_label=1)
        # total_slices = mask_data.shape[0]  # 获取CT的总层数
        # slice_ratio = f"{max_volume_slice_index + 1}/{total_slices}"  # 最大层面输出，+1 是因为索引从0开始
        #
        # # 找到该切片上的最大内切圆
        # mask_slice = mask_data[max_volume_slice_index, :, :] == 1
        # center, max_radius = find_largest_inscribed_circle(mask_slice)
        #
        # # 计算内切圆中的平均CT值
        # ct_slice = ct_data[max_volume_slice_index, :, :]
        # average_ct_value, (rr, cc) = calculate_average_ct_in_circle(ct_slice, center, max_radius)
        #
        # # 计算尺寸和测量指标
        # (transverse_diameter, anteroposterior_diameter, min_x, max_x, max_y_short, top_x,
        #  min_y_ap, max_y_ap, left_length, right_length, left_thickness, right_thickness,
        #  thickness_assist_y, left_thickness_start, left_thickness_end, right_thickness_start,
        #  right_thickness_end, left_length_end, right_length_end) = calculate_diameters_with_type_check(
        #     mask_slice, ct_slice, ct_image.GetSpacing())
        #
        # # 可视化结果
        # visualization_output_folder = config['data']['visualization_output']
        # os.makedirs(visualization_output_folder, exist_ok=True)
        # output_file_path = os.path.join(visualization_output_folder, os.path.basename(ct_file_path).replace('.nii.gz', '_result.png'))
        # plot_combined_results(ct_slice, mask_slice, center, max_radius, average_ct_value,
        #                       transverse_diameter, anteroposterior_diameter, min_x, max_x, max_y_short, top_x,
        #                       min_y_ap, max_y_ap, left_length, right_length, left_thickness, right_thickness,
        #                       left_thickness_start, left_thickness_end, right_thickness_start,
        #                       right_thickness_end, left_length_end, right_length_end, output_file_path)

        # # 收集结果
        # results = {
        #     '文件名': os.path.basename(ct_file_path),
        #     '前后径': anteroposterior_diameter,
        #     '横径': transverse_diameter,
        #     '右叶长度': left_length,
        #     '左叶长度': right_length,
        #     '右叶厚度': left_thickness,
        #     '左叶厚度': right_thickness,
        #     '3D胸腺体积': thymus_volume,
        #     '3D平均CT值': mean_ct_value,
        #     '内切圆平均CT值': average_ct_value,
        #     '最大层面比例': slice_ratio
        # }
        results = {'文件名': 1}

        logger.info(f"完成文件 {ct_file_path} 的处理。")
        return results
    except Exception as e:
        logger.error(f"处理文件 {ct_file_path} 时出错：{e}")
        return None
