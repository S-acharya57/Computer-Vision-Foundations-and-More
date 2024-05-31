import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def contrast_manipulation(img):
    pass 


def create_histogram(color_channel):
    hist = np.zeros(256)
    for pixel in  color_channel.flatten():
        hist[pixel] += 1 
    return hist


def plot_hist(img):
    r,g,b = cv.split(img)
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