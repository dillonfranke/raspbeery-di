from skimage import filters
from skimage import color
from skimage import exposure
from skimage import io
from skimage import data


class EdgeDetector:

    def __init__(self, input_image):
        # die_table = io.imread(input_image)
        # TODO: fix this sheiße, since it's only working with one edge detect image
        # self.edge_mask = filters.sobel(die_table)
        # io.imsave('imgs/edge_detect.png', self.edge_mask)
        self.edges = io.imread('imgs/edge_detect.png')