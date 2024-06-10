import cv2 as cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def resize_and_pad(image, size=(300, 300), pad_color=255):
    """
    Resize image while maintaining aspect ratio and pad to target size.
    """
    h, w = image.shape[:2]
    sh, sw = size

    # Scale the image
    aspect = w / h
    if aspect > 1:
        new_w = sw
        new_h = int(new_w / aspect)
    else:
        new_h = sh
        new_w = int(new_h * aspect)
    
    scaled_img = cv2.resize(image, (new_w, new_h))
    
    pad_img = np.full((sh, sw, 3), pad_color, dtype=np.uint8)
    pad_img[(sh - new_h) // 2 : (sh - new_h) // 2 + new_h, (sw - new_w) // 2 : (sw - new_w) // 2 + new_w] = scaled_img

    return pad_img

def binary_mask(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 4: Apply binary threshold
    _, binary_mask = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Optional Step 5: Apply morphological operations
    kernel = np.ones((3,3), np.uint8)
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, kernel)
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)

    return binary_mask


def contrast_manipulation(img):
    pass 

def create_histogram(color_channel):
    hist = np.zeros(256)
    for pixel in  color_channel.flatten():
        hist[pixel] += 1 
    return hist


def plot_hist(img):
    r,g,b = cv2.split(img)
    hist_r = create_histogram(r)
    hist_g = create_histogram(g)
    hist_b = create_histogram(b)

    plt.figure(figsize=(10,6))

    plt.imshow(img)
    plt.title('flower')
    plt.axis('off')

    plt.subplot(2,1,2)
    plt.plot(hist_r, color='r', label='Red')
    plt.plot(hist_g, color='g', label='Green')
    plt.plot(hist_b, color='b', label='Blue')

    plt.legend()
    plt.show() 


























    