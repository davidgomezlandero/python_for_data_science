from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Loads the image "animal.jpeg", cut a square part from it
    and transpose it
    """
    try:
        img = ft_load("animal.jpeg")
        shape = img.shape
        if shape[0] < 400 or shape[1] < 400:
            raise Exception("Error: the height\
                and width of the image must be >= 400")
        y_start = shape[0] // 2 - 200
        y_end = shape[0] // 2 + 200
        x_start = shape[1] // 2 - 200
        x_end = shape[1] // 2 + 200
        new_image = img[y_start:y_end, x_start:x_end, 0:1]
        print(f"The shape of image\
            is : {new_image.shape} or {new_image[:,:,0].shape}")
        print(new_image)
        image = new_image[:, :, 0]
        rows = image.shape[0]
        cols = image.shape[1]

        transposed = np.zeros((cols, rows), dtype=np.uint8)

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = image[i][j]
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap="gray")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
