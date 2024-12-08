import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import time 

def convolve(original_image, kernel):
    """Function to convolve an image with a kernel function

    Arguments:
        original_image -- array of pixels of 3 channels
        kernel -- the filter to be used while convolving
    """
    height, width, channels = original_image.shape 
    k_height, k_width = kernel.shape 

    new_img = np.zeros_like(original_image)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                # summation for a single pixel
                summation = 0
                for m in range(k_height):
                    for n in range(k_width):
                        # assuring kernel indices are within image's boundary
                        if i-m>=0 and j-n>=0:
                            summation  += original_image[i-m][j-n][k] * kernel[m][n]

                new_img[i][j][k] = summation

    return new_img


def convolve_vectorized(original_image, kernel):
    height, width, channels = original_image.shape 
    k_height, k_width = kernel.shape 


    # Pad the image to handle edge cases
    # padded_image = np.pad(original_image, ((k_height // 2, k_height // 2),
    #                                     (k_width // 2, k_width // 2),
    #                                     (0, 0)))

    new_img = np.zeros_like(original_image)


    # decreasing 2 for avoiding the edges 
    # temporary solution for basic code implementation
    for i in range(height-2):
        for j in range(width-2):
            for k in range(channels):
                # summation for a single pixel
                # print(original_image[i:i+k_height,j:j+k_width,k].shape)
                new_img[i][j][k] = np.sum(original_image[i:i+k_height,j:j+k_width,k] * kernel)

    return new_img


# image = cv2.imread('city.png')

# print(image.shape)

# # sobel filter 
# kernel = np.array([[1, 0, -1],
#                   [2, 0, -2],
#                   [1, 0, -1]])

# convolved_image_vectorized = convolve_vectorized(image, kernel)
# print(convolved_image_vectorized.shape)