import torch
import os
import warnings
import torch.nn as nn
import torch.backends.cudnn as cudnn
from osgeo import gdal

from .utils import Creat_model
from .test import process_all_images_in_folder
from ..config.default_test import _C as cfg


def segment_any_rape(args):
    os.environ['CPL_DEBUG'] = 'OFF'
    os.environ['CPL_LOG'] = '/dev/null'
    warnings.filterwarnings('ignore', category=UserWarning, module='torch')

    model = Creat_model(cfg.MODEL).model()
    model = nn.DataParallel(model).cuda()

    checkpoint = torch.load(args.model_path, map_location=torch.device('cpu'))
    model.module.load_state_dict(checkpoint)

    process_all_images_in_folder(args.input_path, model,
                                 num_classes=args.numclass, num_workers=args.num_workers, stride=args.stride, batch_size=args.batch_size)
