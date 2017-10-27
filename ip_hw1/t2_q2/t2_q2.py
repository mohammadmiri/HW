import cv2 as cv
import numpy
import os




class ImageIntensityTransformer:

    def __init__(self):
        self.dark_top_edge = 5
        self.dark_down_edge = 150
        self.gray_left_edge = 30
        self.gray_top_edge = 170
        self.gray_right_edge = 210
        self.bright_down_edge = 200
        self.bright_top_edge = 220

        self.DARK_CONST = 0
        self.GRAY_CONST = 127
        self.BRIGHT_CONST = 255

        self.src_image = None

    def main(self):
        dir = os.path.dirname(__file__)
        self.src_image = cv.imread(dir+'/gs.jpg', 0)
        cv.imshow("image", self.src_image)
        cv.namedWindow("image", 0)
        cv.createTrackbar("dark_top", "image", 5, 255, self.update_dark_top_edge)
        cv.createTrackbar("dark_down", "image", 150, 255, self.update_dark_down_edge)
        cv.createTrackbar("gray_left", "image", 120, 255, self.update_gray_left_edge)
        cv.createTrackbar("gray_top", "image", 170, 255, self.update_gray_top_edge)
        cv.createTrackbar("gray_right", "image", 210, 255, self.update_gray_left_edge)
        cv.createTrackbar("bright_down", "image", 200, 255, self.update_bright_down_edge)
        cv.createTrackbar("bright_top", "image", 220, 255, self.update_bright_top_edge)
        self.update_image()

        cv.waitKey(0)
        cv.destroyAllWindows()

    def convert_to_grayscale(self, image):
        converted_image = numpy.zeros(shape=(len(image), len(image[0]), 3)).astype(int)
        for i in range(0, len(image)):
            for j in range(0, len(image[i])):
                converted_image[i][j] = numpy.empty_like([int(image[i][j][0]), int(image[i][j][0]), int(image[i][j][0])])
        return converted_image


    def get_gray(self, image_cell):
        if type(image_cell) == 'list':
            return image_cell[0]
        else:
            return image_cell


    def set_cell(self, image_cell, value):
        if type(image_cell) == 'list':
            return [value, value, value]
        else:
            return value


    def update_dark_top_edge(self, val):
        print('dark top')
        dark_top_edge = val
        self.update_image()


    def update_dark_down_edge(self, val):
        print('dark down')
        dark_down_edge = val
        self.update_image()


    def update_gray_left_edge(self, val):
        print('gray left')
        gray_left_edge = val
        self.update_image()


    def update_gray_top_edge(self, val):
        print('gray top')
        gray_top_edge = val
        self.update_image()


    def update_gray_right_edge(self, val):
        print('gray right')
        gray_right_edge = val
        self.update_image()


    def update_bright_top_edge(self, val):
        print('bright down')
        bright_top_edge = val
        self.update_image()


    def update_bright_down_edge(self, val):
        print('bright top')
        bright_down_edge = val
        self.update_image()


    def update_image(self):
        for i in range(0, len(self.src_image)):
            for j in range(0, len(self.src_image[0])):
                gray = self.update_contrast(self.src_image[i][j])
                self.src_image[i][j] = gray
        cv.imshow('image', self.src_image)


    def update_contrast(self, gray):
        dark_value = 0
        if gray <= self.dark_top_edge:
            dark_value = 1
        elif gray > self.dark_top_edge and gray <= self.dark_down_edge:
            dark_value = self.get_value(self.dark_top_edge, self.dark_down_edge, 1, 0, gray)
        gray_value = 0
        if gray >= self.gray_left_edge and gray <= self.gray_top_edge:
            gray_value = self.get_value(self.gray_left_edge, self.gray_top_edge, 0, 1, gray)
        elif gray >= self.gray_top_edge and gray <= self.gray_right_edge:
            gray_value = self.get_value(self.gray_top_edge, self.gray_right_edge, 1, 0, gray)
        bright_value = 0
        if gray >= self.bright_down_edge and gray <= self.bright_top_edge:
            bright_value = self.get_value(self.bright_down_edge, self.bright_top_edge, 0, 1, gray)
        elif gray >= self.bright_top_edge:
            bright_value = 1
        value = (self.DARK_CONST * dark_value + self.GRAY_CONST * gray_value + self.BRIGHT_CONST * bright_value) / (
            dark_value + gray_value + bright_value)
        return round(value)


    # calculate value of line starting from point1 to point2 at index "index"
    def get_value(self, point1, point2, value1, value2, index):
        a = (value2 - value1) / (point2 - point1)
        b = value1
        y = a * index + b
        return y


if __name__ == '__main__':
    transformer = ImageIntensityTransformer()
    transformer.main()
