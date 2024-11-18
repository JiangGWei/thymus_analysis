# Thymus Analysis Tool

## 简介

本项目用于自动化处理CT影像数据，提取胸腺的解剖学和放射学特征，包括分割和测量功能。

## 目录结构


## 使用方法

1. **安装依赖**

    ```bash
    pip install -r requirements.txt
    ```

2. **配置项目**

    编辑 `config/config.yaml` 文件，根据您的环境配置路径和参数。

3. **运行分析**

    通过命令行运行主程序：

    ```bash
    python main.py --input data/images/ --output data/results/ --excel data/results/result.xlsx --config config/config.yaml
    ```

    或者使用运行脚本：

    ```bash
    sh scripts/run_analysis.sh
    ```

## nnUNet 设置

确保已正确设置 nnUNet 的环境变量，并完成数据预处理。参考 [nnUNet 设置指南](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/setting_up_paths.md)。

## 依赖

- torch
- nnunetv2
- SimpleITK
- numpy
- scipy
- matplotlib
- scikit-image
- pandas
- PyYAML
- tqdm
- openpyxl
