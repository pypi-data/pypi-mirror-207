from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import logging
import time
import math
import warnings
from pathlib import Path

import numpy as np

import torch
import torch.nn as nn
from torch.optim.lr_scheduler import _LRScheduler


class Creat_model(object):
    def __init__(self, cfg):
        self.cfg = cfg
        pass

    def model(self):
        if self.cfg.NAME == 'HRNet':
            from model.HRNet.lib.models.seg_hrnet import get_seg_model
            return get_seg_model()

        elif self.cfg.NAME == 'MPSegNet':
            from model.MPSegNet.MPSegNet import Net
            # from model.softnet.MPSegNet_S import Net
            # from model.softnet.MPSegNet_P import Net
            return Net(self.cfg.NUM_CLASSES)

        elif self.cfg.NAME == 'DeepLab':
            from model.net.deeplabv3plus import deeplabv3plus
            return deeplabv3plus(self.cfg.NUM_CLASSES)

        elif self.cfg.NAME == 'PSPNet':
            # from model.PSPNet.pspnet import PSPNet
            from model.pspnet1.nets.pspnet import PSPNet
            return PSPNet(self.cfg.NUM_CLASSES)

        elif self.cfg.NAME == 'UNet':
            from model.unet.unet_model import UNet
            return UNet(self.cfg.IN_CHANNEL, self.cfg.NUM_CLASSES)

        elif self.cfg.NAME == 'FCN':
            from model.FCN_8s.FCN_ResNet import FCN_ResNet
            return FCN_ResNet(self.cfg.NUM_CLASSES)

        elif self.cfg.NAME == 'SwinUNet':
            from ..model.SwinUNet.vision_transformer import SwinUnet as ViT_seg
            from ..config.default import get_cfg

            import rape_identification
            project_root = os.path.dirname(os.path.abspath(rape_identification.__file__))

            # 使用绝对路径加载配置文件
            model_config = get_cfg(os.path.join(project_root, 'config', 'GID.yaml'))

            # model_config = get_cfg('..config/GID.yaml')
            return ViT_seg(model_config)


class SegmentationMetric(object):
    def __init__(self, numClass):
        self.numClass = numClass
        self.confusionMatrix = np.zeros((self.numClass,) * 2)

    def pixelAccuracy(self):
        # return all class overall pixel accuracy
        #  PA = acc = (TP + TN) / (TP + TN + FP + TN)
        acc = np.diag(self.confusionMatrix).sum() / self.confusionMatrix.sum()
        return acc

    def classPixelAccuracy(self):
        # return each category pixel accuracy(A more accurate way to call it precision)
        # acc = (TP) / TP + FP
        classAcc = np.diag(self.confusionMatrix) / self.confusionMatrix.sum(axis=1)
        return classAcc  # 返回的是一个列表值，如：[0.90, 0.80, 0.96]，表示类别1 2 3各类别的预测准确率

    def meanPixelAccuracy(self):
        classAcc = self.classPixelAccuracy()
        meanAcc = np.nanmean(classAcc)  # np.nanmean 求平均值，nan表示遇到Nan类型，其值取为0
        return meanAcc  # 返回单个值，如：np.nanmean([0.90, 0.80, 0.96, nan, nan]) = (0.90 + 0.80 + 0.96） / 3 =  0.89

    def meanIntersectionOverUnion(self):
        # Intersection = TP Union = TP + FP + FN
        # IoU = TP / (TP + FP + FN)
        intersection = np.diag(self.confusionMatrix)  # 取对角元素的值，返回列表
        union = np.sum(self.confusionMatrix, axis=1) + np.sum(self.confusionMatrix, axis=0) - np.diag(
            self.confusionMatrix)  # axis = 1表示混淆矩阵行的值，返回列表； axis = 0表示取混淆矩阵列的值，返回列表
        IoU = intersection / (union + 1e-20)  # 返回列表，其值为各个类别的IoU
        # print('IoU: ', IoU)
        mIoU = np.nanmean(IoU)  # 求各类别IoU的平均
        return mIoU, IoU

    def genConfusionMatrix(self, imgPredict, imgLabel):  # 同FCN中score.py的fast_hist()函数
        # remove classes from unlabeled pixels in gt image and predict
        mask = (imgLabel >= 0) & (imgLabel < self.numClass)
        label = self.numClass * imgLabel[mask] + imgPredict[mask]
        count = np.bincount(label, minlength=self.numClass ** 2)
        confusionMatrix = count.reshape(self.numClass, self.numClass)
        return confusionMatrix

    def Frequency_Weighted_Intersection_over_Union(self):
        # FWIOU =     [(TP+FN)/(TP+FP+TN+FN)] *[TP / (TP + FP + FN)]
        freq = np.sum(self.confusionMatrix, axis=1) / np.sum(self.confusionMatrix)
        iu = np.diag(self.confusionMatrix) / (
                np.sum(self.confusionMatrix, axis=1) + np.sum(self.confusionMatrix, axis=0) -
                np.diag(self.confusionMatrix))
        FWIoU = (freq[freq > 0] * iu[freq > 0]).sum()
        return FWIoU

    def addBatch(self, imgPredict, imgLabel):
        assert imgPredict.shape == imgLabel.shape
        self.confusionMatrix += self.genConfusionMatrix(imgPredict, imgLabel)

    def reset(self):
        self.confusionMatrix = np.zeros((self.numClass, self.numClass))


class SegmentationMetric1(object):
    def __init__(self, numClass):
        self.numClass = numClass
        self.confusionMatrix = torch.zeros((self.numClass,) * 2).cuda()

    def pixelAccuracy(self):
        # return all class overall pixel accuracy
        #  PA = acc = (TP + TN) / (TP + TN + FP + TN)
        acc = torch.diag(self.confusionMatrix).sum() / self.confusionMatrix.sum()
        return acc

    def classPixelAccuracy(self):
        # return each category pixel accuracy(A more accurate way to call it precision)
        # acc = (TP) / TP + FP
        classAcc = torch.diag(self.confusionMatrix) / self.confusionMatrix.sum(axis=1)
        return classAcc  # 返回的是一个列表值，如：[0.90, 0.80, 0.96]，表示类别1 2 3各类别的预测准确率

    def meanPixelAccuracy(self):
        classAcc = self.classPixelAccuracy()
        meanAcc = torch.nanmean(classAcc)  # np.nanmean 求平均值，nan表示遇到Nan类型，其值取为0
        return meanAcc  # 返回单个值，如：np.nanmean([0.90, 0.80, 0.96, nan, nan]) = (0.90 + 0.80 + 0.96） / 3 =  0.89

    def meanIntersectionOverUnion(self):
        # Intersection = TP Union = TP + FP + FN
        # IoU = TP / (TP + FP + FN)
        intersection = torch.diag(self.confusionMatrix)  # 取对角元素的值，返回列表
        union = torch.sum(self.confusionMatrix, dim=1) + torch.sum(self.confusionMatrix, dim=0) - torch.diag(
            self.confusionMatrix)  # axis = 1表示混淆矩阵行的值，返回列表； axis = 0表示取混淆矩阵列的值，返回列表
        IoU = intersection / (union + 1e-20)  # 返回列表，其值为各个类别的IoU
        # mIoU = torch.nanmean(IoU)  # 求各类别IoU的平均
        return IoU

    def genConfusionMatrix(self, imgPredict, imgLabel):  # 同FCN中score.py的fast_hist()函数
        # remove classes from unlabeled pixels in gt image and predict
        mask = (imgLabel >= 0) & (imgLabel < self.numClass)
        label = self.numClass * imgLabel[mask] + imgPredict[mask]
        # label = self.numClass * imgLabel + imgPredict
        count = torch.bincount(label, minlength=self.numClass ** 2)
        confusionMatrix = count.reshape(self.numClass, self.numClass).cuda()
        return confusionMatrix

    def Frequency_Weighted_Intersection_over_Union(self):
        # FWIOU =     [(TP+FN)/(TP+FP+TN+FN)] *[TP / (TP + FP + FN)]
        freq = torch.sum(self.confusionMatrix, dim=1) / torch.sum(self.confusionMatrix)
        iu = torch.diag(self.confusionMatrix) / (
                torch.sum(self.confusionMatrix, dim=1) + torch.sum(self.confusionMatrix, dim=0) -
                torch.diag(self.confusionMatrix) + 1e-20)
        FWIoU = (freq[freq > 0] * iu[freq > 0]).sum()
        return FWIoU

    def addBatch(self, imgPredict, imgLabel):
        assert imgPredict.shape == imgLabel.shape

        self.confusionMatrix += self.genConfusionMatrix(imgPredict, imgLabel)

    def reset(self):
        self.confusionMatrix = np.zeros((self.numClass, self.numClass))


class CosineAnnealingLRWarmup(_LRScheduler):
    def __init__(self, optimizer, T_max, eta_min=1.0e-5, last_epoch=-1, verbose=False,
                 warmup_steps=2, warmup_start_lr=1.0e-5):
        self.T_max = T_max
        self.eta_min = eta_min
        super(CosineAnnealingLRWarmup, self).__init__(optimizer, last_epoch, verbose)
        self.warmup_steps=warmup_steps
        self.warmup_start_lr = warmup_start_lr
        if warmup_steps>0:
            self.base_warup_factors = [
                (base_lr/warmup_start_lr)**(1.0/self.warmup_steps)
                for base_lr in self.base_lrs
            ]

    def get_lr(self):
        if not self._get_lr_called_within_step:
            warnings.warn("To get the last learning rate computed by the scheduler, "
                          "please use `get_last_lr()`.", UserWarning)
        return self._get_closed_form_lr()

    def _get_closed_form_lr(self):
        if hasattr(self,'warmup_steps'):
            if self.last_epoch<self.warmup_steps:
                return [self.warmup_start_lr*(warmup_factor**self.last_epoch)
                        for warmup_factor in self.base_warup_factors]
            else:
                return [self.eta_min + (base_lr - self.eta_min) *
                        (1 + math.cos(math.pi * (self.last_epoch - self.warmup_steps) / (self.T_max - self.warmup_steps)))*0.5
                        for base_lr in self.base_lrs]
        else:
            return [self.eta_min + (base_lr - self.eta_min) *
                    (1 + math.cos(math.pi * self.last_epoch / self.T_max)) / 2
                    for base_lr in self.base_lrs]


class LR_Scheduler(object):
    """Learning Rate Scheduler

    Step mode: ``lr = baselr * 0.1 ^ {floor(epoch-1 / lr_step)}``

    Cosine mode: ``lr = baselr * 0.5 * (1 + cos(iter/maxiter))``

    Poly mode: ``lr = baselr * (1 - iter/maxiter) ^ 0.9``

    Args:
        args:  :attr:`args.lr_scheduler` lr scheduler mode (`cos`, `poly`),
          :attr:`args.lr` base learning rate, :attr:`args.epochs` number of epochs,
          :attr:`args.lr_step`

        iters_per_epoch: number of iterations per epoch
    """
    def __init__(self, args, mode, base_lr, num_epochs, iters_per_epoch=0,
                 lr_step=0, warmup_epochs=0, logger=None):
        self.mode = mode
        self.args = args
        if self.args.local_rank <= 0:
            print('Using {} LR Scheduler!'.format(self.mode))
        self.lr = base_lr
        if mode == 'step':
            assert lr_step
        self.lr_step = lr_step
        self.iters_per_epoch = iters_per_epoch
        self.N = num_epochs * iters_per_epoch
        self.epoch = -1
        self.warmup_iters = warmup_epochs * iters_per_epoch
        # self.logger = logger
        # self.logger.info('Using {} LR Scheduler!'.format(self.mode))

    def __call__(self, optimizer, i, epoch, best_pred):
        T = epoch * self.iters_per_epoch + i
        if self.mode == 'cos':
            lr = 0.5 * self.lr * (1 + math.cos(1.0 * T / self.N * math.pi))
        elif self.mode == 'poly':
            lr = self.lr * pow((1 - 1.0 * T / self.N), 0.9)
        elif self.mode == 'step':
            lr = self.lr * (0.1 ** (epoch // self.lr_step))
        else:
            raise NotImplemented
        # warm up lr schedule
        if self.warmup_iters > 0 and T < self.warmup_iters:
            lr = lr * 1.0 * T / self.warmup_iters
        if epoch > self.epoch and self.args.local_rank <= 0:
            # print('\n=>Epoches %i, learning rate = %.5f, previous best = %.4f ' % (epoch, lr, best_pred*100))
            self.epoch = epoch
        assert lr >= 0
        self._adjust_learning_rate(optimizer, lr)

    def _adjust_learning_rate(self, optimizer, lr):
        if len(optimizer.param_groups) == 1:
            optimizer.param_groups[0]['lr'] = lr
        else:
            # enlarge the lr at the head
            optimizer.param_groups[-1]['lr'] = lr
            for i in range(0, len(optimizer.param_groups)-1):
                optimizer.param_groups[i]['lr'] = lr * 0.1




def create_logger(cfg, cfg_name, phase='train'):
    root_output_dir = Path(cfg.OUTPUT_DIR)
    # set up logger
    if not root_output_dir.exists():
        print('=> creating {}'.format(root_output_dir))
        root_output_dir.mkdir()

    dataset = cfg.DATASETS.DATASET
    model = cfg.MODEL.NAME
    cfg_name = os.path.basename(cfg_name).split('.')[0]

    final_output_dir = root_output_dir / 'Logger' / cfg_name

    print('=> creating {}'.format(final_output_dir))
    final_output_dir.mkdir(parents=True, exist_ok=True)

    time_str = time.strftime('%Y-%m-%d-%H-%M')
    log_file = '{}_{}_{}.log'.format(cfg_name, time_str, phase)
    final_log_file = final_output_dir / log_file
    head = '%(asctime)-15s %(message)s'
    logging.basicConfig(filename=str(final_log_file),
                        format=head)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    logging.getLogger('').addHandler(console)

    tensorboard_log_dir = Path(cfg.OUTPUT_DIR) / 'tensorboardX' / model / \
            (cfg_name + '_' + time_str)
    print('=> creating {}'.format(tensorboard_log_dir))
    tensorboard_log_dir.mkdir(parents=True, exist_ok=True)

    return logger, str(tensorboard_log_dir)
    # return logger, str(final_output_dir), str(tensorboard_log_dir)


def scale_softmax(x):
    x = np.array(x)
    x[x > 1] = 2 - x[x > 1]
    x_row_max = x.max(axis=-1)
    x_row_max = x_row_max.reshape(list(x.shape)[:-1]+[1])
    x = x - x_row_max
    x_exp = np.exp(x)
    x_exp_row_sum = x_exp.sum(axis=-1).reshape(list(x.shape)[:-1]+[1])
    softmax = x_exp / x_exp_row_sum

    return softmax