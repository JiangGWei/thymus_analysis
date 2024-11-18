# segmentation.py

import os
import torch
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
import logging
from src.utils import setup_logger

logger = setup_logger(__name__)

def segment_ct_file(ct_file_path, output_folder, config):
    """
    对单个CT文件进行分割，并返回分割掩码的路径。
    """
    try:
        # 初始化预测器
        predictor = nnUNetPredictor(
            tile_step_size=config['segmentation']['tile_step_size'],
            use_gaussian=config['segmentation']['use_gaussian'],
            use_mirroring=config['segmentation']['use_mirroring'],
            perform_everything_on_device=config['segmentation']['perform_everything_on_device'],
            device=torch.device(config['segmentation']['device']),
            verbose=config['segmentation']['verbose'],
            verbose_preprocessing=config['segmentation']['verbose_preprocessing'],
            allow_tqdm=config['segmentation']['allow_tqdm']
        )

        # 指定模型路径
        trained_model_folder = config['segmentation']['trained_model_folder']

        # 初始化模型
        predictor.initialize_from_trained_model_folder(
            trained_model_folder,
            use_folds=tuple(config['segmentation']['use_folds']),
            checkpoint_name=config['segmentation']['checkpoint_name']
        )

        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)

        # 构建输出文件的路径
        input_filename = os.path.basename(ct_file_path)
        # 去掉 '_0000' 后缀（如果有），并替换扩展名为 '.nii.gz'
        output_filename = input_filename.replace('_0000', '')
        if not output_filename.endswith('.nii.gz'):
            output_filename = os.path.splitext(output_filename)[0] + '.nii.gz'
        predicted_mask_path = os.path.join(output_folder, output_filename)

        # 进行预测，指定输出文件名
        predictor.predict_from_files(
            list_of_lists_or_source_folder=[[ct_file_path]],
            output_folder_or_list_of_truncated_output_files=[predicted_mask_path],
            save_probabilities=config['segmentation']['save_probabilities'],
            overwrite=config['segmentation']['overwrite'],
            num_processes_preprocessing=config['segmentation']['num_processes_preprocessing'],
            num_processes_segmentation_export=config['segmentation']['num_processes_segmentation_export'],
            folder_with_segs_from_prev_stage=None,
            num_parts=config['segmentation']['num_parts'],
            part_id=config['segmentation']['part_id']
        )

        logger.info(f"生成分割掩码: {predicted_mask_path}")
        return predicted_mask_path

    except Exception as e:
        logger.error(f"分割文件{ct_file_path}时出错：{e}")
        return None
