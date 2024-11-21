# main.py

import os
import logging
import pandas as pd
from tqdm import tqdm

from src.utils import load_config, setup_logger, set_environment_variables
import argparse
from processing import process_ct_file
def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Thymus Segmentation and Measurement Tool")
    parser.add_argument('--config', type=str, default='config/config.yaml', help='配置文件路径')
    parser.add_argument('--input', type=str, required=True, help='输入CT文件或文件夹路径')
    parser.add_argument('--output', type=str, default='data/results/', help='输出结果文件夹')
    parser.add_argument('--excel', type=str, default='data/results/result.xlsx', help='结果Excel文件路径')
    args = parser.parse_args()

    # 加载配置
    config = load_config(args.config)

    set_environment_variables(config)
    # 设置日志记录
    logger = setup_logger('thymus_analysis', config['logging']['log_file'])
    logger.info("启动胸腺分析工具。")

    # 检查输入路径
    input_path = args.input
    if not os.path.exists(input_path):
        logger.error(f"输入路径 {input_path} 不存在。")
        return

    # 准备输出文件夹
    output_dir = args.output
    os.makedirs(output_dir, exist_ok=True)

    # 准备Excel结果
    results = []

    # 处理单个文件或多个文件
    if os.path.isfile(input_path):
        ct_files = [input_path]
    else:
        ct_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.nii') or f.endswith('.nii.gz')]

    logger.info(f"找到 {len(ct_files)} 个CT文件需要处理。")

    for ct_file in tqdm(ct_files, desc="Processing CT files"):
        result = process_ct_file(ct_file, config, logger)
        if result:
            results.append(result)

    # 将结果写入Excel文件
    if results:
        df = pd.DataFrame(results)
        os.makedirs(os.path.dirname(args.excel), exist_ok=True)
        df.to_excel(args.excel, index=False)
        logger.info(f"所有结果已写入 {args.excel}")
    else:
        logger.warning("没有结果可写入Excel文件。")

    logger.info("胸腺分析工具完成。")

if __name__ == '__main__':
    main()
