import my_cv
import cv2

demo_img = cv2.imread('flowers/bougainvillea_00014.jpg')

my_cv.plot_hist(demo_img)

print(my_cv)
