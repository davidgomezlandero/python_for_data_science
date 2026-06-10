import numpy as np
# import matplotlib.pyplot as plt
# from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the colors of the image"""
    return 255 - array


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel"""
    return array * [1, 0, 0]


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel"""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0

    return result


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel"""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0

    return result


def ft_grey(array) -> np.ndarray:
    """Converts image to greyscale."""
    result = array.copy()
    grey = (array[:, :, 0] / 3) + (array[:, :, 1] / 3) + (array[:, :, 2] / 3)
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result.astype(np.uint8)


""" if __name__ == "__main__":
    try:
        array = ft_load("landscape.jpg")
        invert_image = ft_invert(array)

        filters = {
            "Figure VIII.1: Original": array,
            "Figure VIII.2: Invert": ft_invert(array),
            "Figure VIII.3: Red": ft_red(array),
            "Figure VIII.4: Green": ft_green(array),
            "Figure VIII.5: Blue": ft_blue(array),
            "Figure VIII.6: Grey": ft_grey(array)}

        fig, axes = plt.subplots(3, 2, figsize=(16, 12))
        axes = axes.flatten()

        for idx, (title, img) in enumerate(filters.items()):
            axes[idx].imshow(img)
            axes[idx].set_xlabel(title, fontsize=16)
            axes[idx].set_xticks([])
            axes[idx].set_yticks([])

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(e)
 """
