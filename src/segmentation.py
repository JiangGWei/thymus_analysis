# segmentation.py

import os
import torch
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
import logging
from src.utils import setup_logger

logger = setup_logger(__name__)

def segment_ct_file(ct_file_path, output_folder, config):

        return 0
