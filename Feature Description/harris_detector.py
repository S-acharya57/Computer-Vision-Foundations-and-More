# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:43:09 2024

@author: OMEN
"""

import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt 
from scipy.ndimage import gaussian_filter

img_file = cv.imread("../chess2.jpg")
gray = cv.cvtColor(img_file,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

# k = harris parameter
harris = cv.cornerHarris(gray, blockSize=2, ksize=3, k=0.08)


# =============================================================================
# HARRIS CORNER DETECTION WITHOUT LIBRARY
# 1. Gradient Computation
# 2. Structure Tensor Matrix
# 3. Corner Response Function
# 4. Thresholding
# =============================================================================

k = 0.08
threshold = 0.01

I_x = cv.Sobel(gray, cv.CV_64F, dx=1, dy=0, ksize=3)
I_y = cv.Sobel(gray, cv.CV_64F, dx=0, dy=1, ksize=3)

# product of gradients
I_x2 = I_x ** 2
I_y2 = I_y ** 2
I_xy = I_x * I_y

# for smoothing! 
S_xx = gaussian_filter(I_x2, sigma=1)
S_yy = gaussian_filter(I_y2, sigma=1)
S_xy = gaussian_filter(I_xy, sigma=1)

# determinant
det = (S_xx * S_yy) - (2*S_xy)
trace = S_xx + S_yy

# Corner Response Function
R = det - (k * (trace**2))

corners_opencv = np.zeros_like(harris)
corners_manual = np.zeros_like(R)

corners_opencv[harris > threshold * harris.max()] = 1
corners_manual[R > threshold * R.max()] = 1


comparison_image = img_file.copy()
# comparison_image[corners_opencv == 1] = [255, 0, 0] # (red)
comparison_image[corners_manual == 1] = [0, 255, 0] # (green)


distance = np.mean((harris - R) ** 2)
print(distance)
plt.imshow(comparison_image)

