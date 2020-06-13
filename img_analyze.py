from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data
import numpy as np
import matplotlib.pyplot as plt



die_table = io.imread('imgs/IMG_2834.jpg')

edges = filters.sobel(die_table)

io.imsave('test2.png', edges)
