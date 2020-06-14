from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math


def find_color(die_table):
    yellow_rows = []
    yellow_cols = []
    for x in range(die_table.shape[0]):
        for y in range(die_table.shape[1]):
            if die_table[x][y][1] > 180:
                yellow_rows.append(x)
                yellow_cols.append(y)
    return yellow_rows, yellow_cols


def on_table_rows(x):
    edges = io.imread('imgs/edge_detect.png')
    row_color = []
    for i in range(edges.shape[1]):
        row_color.append(np.sum(edges[x][i])-255)
    return np.mean(row_color) > 50


def on_table_cols(y):
    edges = io.imread('imgs/edge_detect.png')
    col_color = []
    for i in range(edges.shape[0]):
        col_color.append(np.sum(edges[i][y])-255)
    return np.mean(col_color) > 50


def find_row(yellow_rows):
    row_val = 0
    largest_count = 0
    row_counts = Counter(yellow_rows)
    for row in row_counts.keys():
        if(on_table_rows(row) and row_counts[row] > largest_count):
            row_val = row
            largest_count = row_counts[row]
    return row_val


def find_col(yellow_cols):
    col_val = 0
    largest_count = 0
    col_counts = Counter(yellow_cols)
    for col in col_counts.keys():
        if(on_table_cols(col) and col_counts[col] > largest_count):
            col_val = col
            largest_count = col_counts[col]
    return col_val


if __name__ == '__main__':
    die_table = io.imread('imgs/IMG_2834.jpg')
    yellow_rows, yellow_cols = find_color(die_table)
    row = find_row(yellow_rows)
    col = find_col(yellow_cols)
    print(col, row)
