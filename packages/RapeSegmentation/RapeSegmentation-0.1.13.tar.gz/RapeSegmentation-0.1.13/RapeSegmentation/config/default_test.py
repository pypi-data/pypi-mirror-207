from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from yacs.config import CfgNode as CN

_C = CN()

_C.OUTPUT_DIR = ''
_C.LOG_DIR = ''
_C.GPUS = (0, )
_C.WORKERS = 8
_C.BATCH_SIZE_PER_GPU = 8

_C.MODEL = CN()
_C.MODEL.NAME = 'SwinUNet'
_C.MODEL.IN_CHANNEL = 5
_C.MODEL.NUM_CLASSES = 2
_C.MODEL.NUM_OUTPUTS = 1
_C.MODEL.LOAD = '/home/yangping/new/Save/model/SwinUNet/SwinU-GID-HS_WFV_84.87_49_44.pt'
# _C.MODEL.LOAD = '/home/yangping/new/Save/P-A3-91.0_92.1_OA_87.5032_180_600.pkl'
# _C.MODEL.LOAD = '/home/yangping/new/Save/P-A5-91.38_92.43_OA_88.0432_187_500.pkl'
_C.MODEL.MODEL_PATH = 'Save/'
# _C.MODEL.RESULT_PATH = None
_C.MODEL.RESULT_PATH = '/home/yangping/尺度相似可视化/P-V/'

_C.TEST = CN()
_C.TEST.LOAD_PT = False
_C.TEST.FLIP_IMG = True
_C.TEST.NUM_IMG = 1
_C.TEST.IMG_SIZE = [224, 224]
_C.TEST.STRIDE = 64
_C.TEST.MULTI_SCALE = [1]
# _C.TEST.MULTI_SCALE = [0.75, 1, 1.15, 1.2]
_C.TEST.MULTI_SCALE_WEIGHT = False
# _C.TEST.MULTI_SCALE_WEIGHTS = [0.85, 1, 1.15]
_C.TEST.INTERPOLATE_MODE = 'bicubic'
_C.TEST.SAVE_NAME = 'JS_SwinUPre_.tif'
_C.TEST.SAVE_LAB = 'JS_WFV411_NDVI_Lab.tif'

_C.DATASETS = CN()
_C.DATASETS.DATASET = 'GID'
_C.DATASETS.SCALE_R = 2
_C.DATASETS.CROP_SIZE = [256, 256]
_C.DATASETS.RE_SIZE = [256, 256]
# _C.DATASETS.ROOT = '/GID/WFV/WFV_411/'
_C.DATASETS.ROOT = '/GID/GF/'

_C.CUDNN = CN()
_C.CUDNN.BENCHMARK = True
_C.CUDNN.DETERMINISTIC = False
_C.CUDNN.ENABLED = True


def get_cfg_defaults():
  return _C.clone()


def get_cfg(cfg_case=None):
    cfg = get_cfg_defaults()
    if cfg_case is not None:
        cfg.merge_from_file(cfg_case)
    cfg.freeze()
    return cfg


def update_config(cfg, args):
    cfg.defrost()

    cfg.merge_from_file(args.cfg)
    cfg.merge_from_list(args.opts)

    cfg.freeze()
