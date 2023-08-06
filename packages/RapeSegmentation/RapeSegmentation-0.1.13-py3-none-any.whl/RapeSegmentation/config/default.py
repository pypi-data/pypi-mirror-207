from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os


from yacs.config import CfgNode as CN


_C = CN()

_C.OUTPUT_DIR = ''
_C.LOG_DIR = ''
_C.GPUS = (0, 1)
_C.WORKERS = 8
_C.BASE_LR = 0.01
_C.BATCH_SIZE_PER_GPU = 16
_C.OUTPUT_DIR = 'Save/'


_C.MODEL = CN()
_C.MODEL.NAME = 'UNet'
_C.MODEL.IN_CHANNEL = 5
_C.MODEL.NUM_CLASSES = 2
_C.MODEL.NUM_OUTPUTS = 1
_C.MODEL.ALIGN_CORNERS = True
_C.MODEL.LOAD = None
_C.MODEL.MODEL_PATH = 'Save/GF/'

# SwinUNet

_C.MODEL.SWIN = CN()
_C.MODEL.SWIN.TYPE = 'swin'
_C.MODEL.SWIN.NAME = 'swin_base_patch4_window7_224'
_C.MODEL.SWIN.DROP_PATH_RATE = 0.1
_C.MODEL.SWIN.PATCH_SIZE = 4
_C.MODEL.SWIN.EMBED_DIM = 96
_C.MODEL.SWIN.DEPTHS = [2, 2, 6, 2]
_C.MODEL.SWIN.DECODER_DEPTHS = [2, 2, 2, 1]
_C.MODEL.SWIN.NUM_HEADS = [3, 6, 12, 24]
_C.MODEL.SWIN.WINDOW_SIZE = 7
_C.MODEL.SWIN.MLP_RATIO = 4.
_C.MODEL.SWIN.QKV_BIAS = True
_C.MODEL.SWIN.QK_SCALE = None
_C.MODEL.SWIN.DROP_RATE = 0.0
_C.MODEL.SWIN.DROP_PATH_RATE = 0.1
_C.MODEL.SWIN.APE = False
_C.MODEL.SWIN.PATCH_NORM = True
_C.MODEL.SWIN.USE_CHECKPOINT = False
_C.MODEL.SWIN.PRETRAIN_CKPT = '/home/yangping/new/model/SwinUNet/swin_base_patch4_window7_224_22k.pth'

_C.LOSS = CN()
_C.LOSS.USE_OHEM = True
_C.LOSS.OHEMTHRES = 0.9
_C.LOSS.OHEMKEEP = 100000
_C.LOSS.CLASS_BALANCE = False
_C.LOSS.BALANCE_WEIGHTS = [1]
_C.LOSS.IGNORE_INDEX = 0


_C.DATASETS = CN()
_C.DATASETS.DATASET = 'GRSS'
_C.DATASETS.SCALE_R = 2
_C.DATASETS.IMG_SIZE = 224
_C.DATASETS.CROP_SIZE = [224, 224]
_C.DATASETS.RE_SIZE = [224, 224]
_C.DATASETS.ROOT = '/home/yangping/Datasets/GID/WFV/'
# _C.DATASETS.TRANSFORM = transforms


_C.TRAIN = CN()
_C.TRAIN.SEED = 1234
_C.TRAIN.SHUFFLE = None


_C.TRAIN.EPOCH = [0, 100]
_C.TRAIN.PRINT_FREQ = 2
_C.TRAIN.Val_FREQ = [180, 2, 650]
_C.TRAIN.BEST_ACC = 0

_C.TRAIN.OPTIM = 'SGD'
_C.TRAIN.SCHEDULER = 'poly'


_C.CUDNN = CN()
_C.CUDNN.BENCHMARK = False
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
