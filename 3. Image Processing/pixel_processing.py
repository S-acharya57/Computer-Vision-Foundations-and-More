import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

def change_brightness(image_path, brightness_level:int):
    """Function to change the brightness of image with pixel level operation
    Pixels are added by the brightness level

    Arguments:
        image -- path of the image to read
        brightness_level -- level of brightness for the new image
    """
    img = cv2.imread(image_path)
    height, width, channels = img.shape 
    new_img = np.zeros_like(img)

    # looping across all the pixels for all channels
    for i in range(height):
        for j in range(width):
            for k in range(channels):

                # new pixel value
                pixel = img[i][j][k] + brightness_level
                
                # ensuring it stays within 0-255
                pixel = max(0, min(255, pixel))
                new_img[i][j][k] = pixel 

    return new_img


def change_contrast(image_path, contrast_level:int):
    """Function to change the contrast of image with pixel level operation
    Pixels are multiplied by the contrast level

    Arguments:
        image -- path of the image to read
        brightness_level -- level of brightness for the new image
    """
    img = cv2.imread(image_path)
    height, width, channels = img.shape 
    new_img = np.zeros_like(img)

    # looping across all the pixels for all channels
    for i in range(height):
        for j in range(width):
            for k in range(channels):

                # new pixel value
                pixel = img[i][j][k] * contrast_level
                
                # ensuring it stays within 0-255
                pixel = max(0, min(255, pixel))
                new_img[i][j][k] = pixel 

    return new_img
