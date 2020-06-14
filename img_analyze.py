from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data
import numpy as np
import matplotlib.pyplot as plt


die_table = io.imread('imgs/IMG_2834.jpg')

num = 0
for x in die_table:
    for y in x:
        if y[1] > 180:
            num += 1
        

print(num)
