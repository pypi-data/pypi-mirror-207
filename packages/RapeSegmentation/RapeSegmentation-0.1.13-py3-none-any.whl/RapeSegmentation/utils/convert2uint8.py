import tifffile
from PIL import Image
from osgeo import gdal
import numpy as np
import tifffile as tiff
import re
import os


def get_stretch_scale(array):
    """计算2%、98%的值"""
    per2 = np.percentile(array, 2)
    per98 = np.percentile(array, 98)
    # 最小值，最大值映射到0-255
    return per2, per98, (per98 - per2) / 255


def read_tif(_tif):
    """读取tif数据"""
    _ds: gdal.Dataset = gdal.Open(_tif)
    _prj = _ds.GetProjection()
    _transform = _ds.GetGeoTransform()
    return _ds, _prj, _transform


def save2tif(array, prj, transform, out_tif):
    """保存为tif"""
    rows, cols, _ = array.shape
    tif_driver: gdal.Driver = gdal.GetDriverByName('GTiff')
    tif_ds: gdal.Dataset = tif_driver.Create(out_tif, cols, rows, 3, gdal.GDT_Byte)
    # 设置投影和坐标信息
    tif_ds.SetProjection(prj)
    tif_ds.SetGeoTransform(transform)
    # 获取波段
    b1: gdal.Band = tif_ds.GetRasterBand(1)
    b2: gdal.Band = tif_ds.GetRasterBand(2)
    b3: gdal.Band = tif_ds.GetRasterBand(3)

    # 设置无效值
    b1.SetNoDataValue(0)
    b2.SetNoDataValue(0)
    b3.SetNoDataValue(0)

    # 写入数据
    b1.WriteArray(array[:, :, 0])
    b2.WriteArray(array[:, :, 1])
    b3.WriteArray(array[:, :, 2])

    # if _ == 4:
    #     b4: gdal.Band = tif_ds.GetRasterBand(4)
    #     b4.SetNoDataValue(0)
    #     b4.WriteArray(array[3])


def convert2uint8(_tif):

    ds, prj, transform = read_tif(_tif)
    array = ds.ReadAsArray()
    if array.dtype == 'uint16' or array.dtype == 'int16':
        for i in range(array.shape[0]):
            per2, per98, scale = get_stretch_scale(ds.GetRasterBand(i + 1).ReadAsArray())
            i_array = array[i]
            i_array[i_array < per2] = per2
            i_array[i_array > per98] = per98
            # 数组拉伸
            array[i] = (i_array - per2) / scale
        # 转为uint8
        array = np.uint8(array)

        _tif = os.path.basename(_tif)
        # print(_tif)
        if re.match(r'^S[2]_', _tif):
            # print('S2')
            array = array[[3, 0, 1, 2], :, :]
        elif re.match(r'^GF[126]_', _tif):
            # print('GF')
            array = array[[3, 2, 1, 0], :, :]
        elif re.match(r'^HJ[2][A]_', _tif):
            # print('HJ')
            array = array[[4, 2, 1, 0], :, :]
    array = np.transpose(array, (1, 2, 0))
    return array, prj, transform
    # save2tif(array, prj, transform)


if __name__ == '__main__':
    import time

    s = time.time()

    tif = r'HJ2A_CCD_20230314_T50RQV.tif'
    out_tif = tif.replace('.tif', '_docker1.tif')

    convert2uint8(tif)

    t = time.time()
    print(t - s, '秒')
