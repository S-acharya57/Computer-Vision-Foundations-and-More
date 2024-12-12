# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:29:33 2024

@author: OMEN
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
from scipy.ndimage import gaussian_filter

img = cv.imread("../chess2.jpg")
print(img.shape)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# good features to track
corners = cv.goodFeaturesToTrack(gray,maxCorners=250,qualityLevel=0.01,minDistance=10)

# int0 converts the datatype to int64
# int0 is deprecated, int0 is replaced by intp to change into int64
corners2 = np.intp(corners)


# =============================================================================
# Tomasi Filter From Scratch
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

# Getting second moment matrix and response for corners
R_tomasi = np.zeros_like(gray, dtype=np.float32)

for x in range(gray.shape[0]):
    for y in range(gray.shape[1]):
        M = np.array([[S_xx[x, y], S_xy[x, y]],
                      [S_xy[x, y], S_yy[x, y]]])
        
        # eigen values
        eigenvalues = np.linalg.eigvals(M)
        R_tomasi[x, y] = min(eigenvalues)
        
threshold = threshold * R_tomasi.max()
corners_tomasi = (R_tomasi>threshold)

# from the library
opencv_result = img.copy()
if corners is not None:
    for corner in corners:
        x, y = np.intp(corner[0])
        cv.circle(opencv_result, (x, y), 3, (0, 255, 0), -1)

# Visualization
comparison_image = img.copy()
comparison_image[corners_tomasi] = [255, 0, 0]  # Shi-Tomasi (scratch) in red

# resolution of the original image
fig, axes = plt.subplots(1, 2, figsize=(img.shape[1] / 100, img.shape[0] / 100), dpi=100)

# Shi-Tomasi manual result
axes[0].imshow(comparison_image)
axes[0].set_title("Shi-Tomasi - From Scratch (Red)")
axes[0].axis("off")

# OpenCV result
axes[1].imshow(opencv_result)
axes[1].set_title("Shi-Tomasi - From OpenCV (Green)")
axes[1].axis("off")

plt.tight_layout()
plt.show()
