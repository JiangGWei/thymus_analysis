# src/utils.py

import yaml
import logging
import os
def load_config(config_path='config/config.yaml'):
    """
    加载YAML格式的配置文件。
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
    except UnicodeDecodeError as e:
        logging.error(f"配置文件编码错误: {e}")
        raise
    except Exception as e:
        logging.error(f"加载配置文件{config_path}时出错：{e}")
        raise

def setup_logger(name, log_file='logs/app.log', level=logging.INFO):
    """
    设置日志记录器。
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
    handler = logging.FileHandler(log_file, encoding='utf-8')        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger
def set_environment_variables(config):
    """
    根据配置文件设置环境变量。
    """
    os.environ['nnUNet_raw'] = config['data'].get('raw_data', 'data/raw/')
    os.environ['nnUNet_preprocessed'] = config['data'].get('preprocessed_data', 'data/preprocessed/')
    os.environ['nnUNet_results'] = config['data'].get('results_data', 'data/results/')
