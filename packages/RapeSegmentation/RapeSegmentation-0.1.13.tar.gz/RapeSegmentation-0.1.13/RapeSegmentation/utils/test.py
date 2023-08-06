import cv2
import os
import torch
import numpy as np
import torch.nn.functional as F
from tqdm import tqdm
from torch.cuda.amp import autocast
from torch.utils.data import DataLoader

from .convert2uint8 import convert2uint8, save2tif
from ..dataset.SlidingWindowDataset import SlidingWindowDataset


def test_large_image(model, img_path, output_path, num_classes, num_workers, window_size=224, stride=64, batch_size=100, threshold=0.5):
    # Load the large image and create the dataset and dataloader
    array, ds, transform = convert2uint8(img_path)
    dataset = SlidingWindowDataset(img_array=array, window_size=window_size, stride=stride)
    dataloader = DataLoader(dataset,
                            batch_size=batch_size,
                            shuffle=False,
                            num_workers=num_workers,
                            pin_memory=True,
                            # drop_last=False,
                            # prefetch_factor=4,
                            # persistent_workers=True,
                            )

    img_height, img_width = dataset.img.shape[:2]

    # Initialize arrays to accumulate predictions and count the number of predictions per pixel
    prediction_sum = np.zeros((num_classes, img_height, img_width), dtype=np.float32)
    prediction_count = np.zeros((img_height, img_width), dtype=np.int32)

    model.eval()
    with torch.no_grad():
        # for batch_idx, (input_image, input_ndvi) in enumerate(tqdm(dataloader)):
        for batch_idx, (input_image, input_ndvi) in enumerate(dataloader):

            input_image = input_image.cuda()
            input_ndvi = input_ndvi.cuda()

            outputs = model(input_image, ndvi=input_ndvi)
            outputs = F.softmax(outputs, dim=1)
            outputs = outputs.squeeze().detach().cpu().numpy()

            for b in range(outputs.shape[0]):
                y = (b + batch_size * batch_idx) // dataset.num_windows_x
                x = (b + batch_size * batch_idx) % dataset.num_windows_x
                i, j = y * stride, x * stride
                prediction_sum[:, i:i + window_size, j:j + window_size] += outputs[b]
                prediction_count[i:i + window_size, j:j + window_size] += 1

    # Remove padding and restore the original image size
    prediction_sum = prediction_sum[:, :dataset.orig_img_height, :dataset.orig_img_width]
    prediction_count = prediction_count[:dataset.orig_img_height, :dataset.orig_img_width]
    assert np.all(prediction_count > 0), "All elements in prediction_count should be greater than 0."

    # Calculate the average prediction
    # prediction_count[prediction_count == 0] = 1
    prediction_avg = prediction_sum / prediction_count[np.newaxis, :, :]
    # (prediction_avg[2, :, :])[(prediction_avg[2, :, :]) >= threshold] = 1
    segmentation_result = np.argmax(prediction_avg, axis=0)

    a = np.zeros((segmentation_result.shape[0], segmentation_result.shape[1], 3)).astype('uint8')
    a[segmentation_result == 1] = [0, 176, 80]
    save2tif(a, ds, transform, output_path)


def process_all_images_in_folder(input_folder, model, num_workers, num_classes=2, stride=64, batch_size=100):
    # 创建一个新的输出文件夹
    output_folder = input_folder + '_Pre'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        os.chmod(output_folder, 0o777)

    for root, _, files in os.walk(input_folder):
        with tqdm(files) as pbar:
            for file in pbar:
                if file.endswith('.tif'):
                    image_path = os.path.join(root, file)
                    output_filename = file.replace('.tif', '_Pre.tif')
                    output_path = os.path.join(output_folder, output_filename)

                    pbar.set_description(f"处理中的文件：{file}")

                    test_large_image(model, image_path, output_path, num_workers=num_workers,
                                     num_classes=num_classes, stride=stride, batch_size=batch_size)
