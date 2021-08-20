import cv2
from matplotlib import pyplot as plt

KERNEL_SIZE = (5, 5)
SIGMA_VALUES = [0.5, 0.75, 1, 1.25, 1.75]


def display_images(images, titles):
    for i in range(len(images)):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    original_image = cv2.imread("bwimage.jpg")
    images = [original_image]
    titles = ["Original Image"]
    for i in range(len(SIGMA_VALUES)):
        images.append(cv2.GaussianBlur(original_image, KERNEL_SIZE, SIGMA_VALUES[i]))
        titles.append("sigma=%s" % SIGMA_VALUES[i])
    display_images(images, titles)
