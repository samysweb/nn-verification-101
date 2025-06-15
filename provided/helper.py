import numpy as np

import matplotlib.pyplot as plt

def show_image(np_file_path, upscale_factor=8):
    """
    Loads a 3D numpy array from file (shape: 1,28,28), upscales it, and displays it as a greyscale image.
    Args:
        np_file_path (str): Path to the .npy file.
        upscale_factor (int): Factor to upscale the image for better visibility.
    """
    arr = np.load(np_file_path)
    if arr.shape != (1, 28, 28):
        raise ValueError(f"Expected shape (1,28,28), got {arr.shape}")
    img = 1.0-arr[0]
    plt.figure(figsize=(upscale_factor, upscale_factor))
    plt.imshow(img, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.show()