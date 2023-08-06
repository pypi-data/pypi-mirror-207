import numpy as np
import torch
from torch.utils.data import Dataset


class SlidingWindowDataset(Dataset):
    def __init__(self, img_array, window_size=224, stride=64):
        self.window_size = window_size
        self.stride = stride

        # Read the large image
        self.img = img_array
        self.orig_img_height, self.orig_img_width = self.img.shape[:2]

        # Pad image
        img_height, img_width = self.img.shape[:2]
        pad_height = stride
        pad_width = stride
        self.img = np.pad(self.img, ((0, pad_height), (0, pad_width), (0, 0)), mode='reflect')

        self.num_windows_y = (self.img.shape[0] - window_size) // stride + 1
        self.num_windows_x = (self.img.shape[1] - window_size) // stride + 1
        self.total_windows = self.num_windows_y * self.num_windows_x

    def __len__(self):
        return self.total_windows

    def __getitem__(self, idx):
        y = idx // self.num_windows_x
        x = idx % self.num_windows_x

        y_start = y * self.stride
        x_start = x * self.stride

        image = self.img[y_start:y_start + self.window_size, x_start:x_start + self.window_size, :]

        ndvi = self.NDVI(image)
        image = self.input_transform(image)

        image = torch.from_numpy(image)
        ndvi = torch.from_numpy(ndvi).float()

        return image, ndvi

    def NDVI(self, image):
        image = image.astype(np.float32)
        ndvi = (image[:, :, 0] - image[:, :, 1]) / (image[:, :, 0] + image[:, :, 1] + 1e-20)  # NVDI = (IR-R)/(IR+R)
        ndvi = np.expand_dims(ndvi, 0)
        return ndvi

    def input_transform(self, image):
        image = image.astype(np.float32)
        for i in range(image.shape[2]):
            mean = np.mean(image[:, :, i])
            std = np.std(image[:, :, i])
            image[:, :, i] = (image[:, :, i] - mean) / (std + 1e-20)
        image = np.transpose(image, (2, 0, 1))
        return image
