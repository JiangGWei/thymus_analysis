# Thymus Analysis Tool

## synopsis

This project is used to automate the processing of CT image data to extract anatomical and radiological features of the thymus, including segmentation and measurement functions.

##

## Usage

1. **Installation of dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Configuration items**

    Edit the `config/config.yaml` file to configure the path and parameters according to your environment.

3. **Operational analysis**

    Run the main program from the command line:

    ```bash
    python main.py --input data/images/ --output data/results/ --excel data/results/result.xlsx --config config/config.yaml
    ```

    Or use a run script:

    ```bash
    sh scripts/run_analysis.sh
    ```

## nnUNet Settings

Ensure that the environment variables for nnUNet have been set correctly and that data preprocessing has been completed. 
Refer to Refer to [nnUNet Setup Guide].(https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/setting_up_paths.md)。

## Dependencies

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

If you need to split the model parameters, please contact email: jianggw14@midea.com
