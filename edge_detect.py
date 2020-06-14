from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data



die_table = io.imread('imgs/IMG_2834.jpg')

edges = filters.sobel(die_table)

io.imsave('imgs/test2.png', edges)