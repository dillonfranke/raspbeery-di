# Third Part Imports
from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math

# Local Imports
from src.edge_detect import EdgeDetector


class DieTable():

    def __init__(self, img_path):
        self.die_table_image = io.imread(img_path)
        self.edge_detector = EdgeDetector(img_path)
        self.die_row = 0
        self.die_col = 0

    def find_die(self):
        self.yellow_rows, self.yellow_cols = self.find_color(self.die_table_image)
        self.find_row()
        self.find_col()

    def find_color(self, die_table):
        yellow_rows = []
        yellow_cols = []
        for x in range(die_table.shape[0]):
            for y in range(die_table.shape[1]):
                if die_table[x][y][1] > 180:
                    yellow_rows.append(x)
                    yellow_cols.append(y)
        return yellow_rows, yellow_cols


    def is_on_table_row(self, x):
        row_color = []
        for i in range(self.edge_detector.edges.shape[1]):
            row_color.append(np.sum(self.edge_detector.edges[x][i])-255)
        return np.mean(row_color) > 50


    def is_on_table_col(self, y):
        col_color = []
        for i in range(self.edge_detector.edges.shape[0]):
            col_color.append(np.sum(self.edge_detector.edges[i][y])-255)
        return np.mean(col_color) > 50


    def find_row(self):
        row_val = 0
        largest_count = 0
        row_counts = Counter(self.yellow_rows)
        for row in row_counts.keys():
            if(self.is_on_table_row(row) and row_counts[row] > largest_count):
                row_val = row
                largest_count = row_counts[row]
        self.die_row = row_val


    def find_col(self):
        col_val = 0
        largest_count = 0
        col_counts = Counter(self.yellow_cols)
        for col in col_counts.keys():
            if(self.is_on_table_col(col) and col_counts[col] > largest_count):
                col_val = col
                largest_count = col_counts[col]
        self.die_col = col_val