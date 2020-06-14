from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math


def find_x(yellow_rows):
    edges = io.imread('imgs/edge_detect.png')
    row_color = []
    for i in range(edges.shape[0]):
        row_color.append(np.sum(edges[0][i])-255)
    print()
    x_val = 0
    for x in row_counts.keys():
        count = row_counts[x]


die_table = io.imread('imgs/IMG_2834.jpg')

num = 0
yellow_cols = []
yellow_rows = []
for x in range(die_table.shape[0]):
    for y in range(die_table.shape[1]):
        if die_table[x][y][1] > 180:
            yellow_rows.append(x)
            yellow_cols.append(y)

find_x(yellow_rows)
