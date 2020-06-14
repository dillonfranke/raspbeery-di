from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data
import numpy as np
import matplotlib.pyplot as plt


<<<<<<< HEAD
die_table = io.imread('imgs/IMG_2834.jpg', as_gray=True)
filters.sobel(die_table)
io.imsave('test2.png', edges)
=======
die_table = io.imread('imgs/IMG_2834.jpg')

num = 0
for x in die_table:
    for y in x:
        if y[1] > 180:
            num += 1
        

print(num)
>>>>>>> 973d82dbd2e249c30f1235cc211b06bbe14b2793
