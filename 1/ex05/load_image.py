import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Load an image and return its pixel data in RGB format.

    Args:
        path (str): Path to the image file (JPG/JPEG).

    Returns:
        np.ndarray: Image array with shape (height, width, 3).

    Raises:
        Exception: If image cannot be opened or is unsupported format.
    """
    if not os.path.exists(path):
        raise Exception(f"Error: Image file '{path}' not found.")
    valid_extensions = ('.jpg', '.jpeg')
    if not path.lower().endswith(valid_extensions):
        raise Exception(f"Error: File must be\
            JPG or JPEG format. Got '{os.path.splitext(path)[1]}'")
    try:
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        array = np.array(img)
        print(f"The shape of image is: {array.shape}")
        print(array)
        return array
    except Exception as e:
        raise Exception(str(e))
