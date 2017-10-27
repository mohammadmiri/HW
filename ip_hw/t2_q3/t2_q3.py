import cv2 as cv
import matplotlib.pyplot as plt
import os

class ImageIntensityTransformer:

    def __init__(self):
        self.darker_top_right_edge = 5
        self.darker_down_right_edge = 50

        self.dark_down_left_edge = 30
        self.dark_top_left_edge = 50
        self.dark_top_right_edge = 70
        self.dark_down_right_edge = 100

        self.gray_down_left_edge = 80
        self.gray_top_left_edge = 110
        self.gray_top_right_edge = 140
        self.gray_down_right_edge = 180

        self.bright_down_left_edge = 150
        self.bright_top_left_edge = 190
        self.bright_top_right_edge = 200
        self.bright_down_right_edge = 230

        self.brighter_top_left_edge = 220
        self.brighter_down_left_edge = 240

        self.DARKER_CONST = 0
        self.DARK_CONST = 80
        self.GRAY_CONST = 127
        self.BRIGHT_CONST = 200
        self.BRIGHTER_CONST = 255

        self.src_image = None

    def main(self):
        dir = os.path.dirname(__file__)
        self.src_image = cv.imread(dir+'/gs.jpg', 0)
        # cv.imshow("window_image", self.src_image)
        # cv.namedWindow("window_image", 0)
        # cv.createTrackbar("darker_right_top", "image", 5, 255, self.update_darker_top_right_edge)
        # cv.createTrackbar("darker_right_down", "image", 50, 255, self.update_darker_down_right_edge)
        # cv.createTrackbar("dark_down_left_edge", "image", 30, 255, self.update_dark_down_left_edge)
        # cv.createTrackbar("dark_top_left_edge", "image", 50, 255, self.update_dark_top_left_edge)
        # cv.createTrackbar("dark_top_right_edge", "image", 70, 255, self.update_dark_top_right_edge)
        # cv.createTrackbar("dark_down_right_edge", "image", 100, 255, self.update_dark_down_right_edge)
        # cv.createTrackbar("gray_down_left_edge", "image", 80, 255, self.update_gray_down_left_edge)
        # cv.createTrackbar("gray_top_left_edge", "image", 110, 255, self.update_gray_top_left_edge)
        # cv.createTrackbar("gray_top_right_edge", "image", 140, 255, self.update_gray_top_right_edge)
        # cv.createTrackbar("gray_down_right_edge", "image", 180, 255, self.update_gray_down_right_edge)
        # cv.createTrackbar("bright_down_left_edge", "image", 150, 255, self.update_bright_down_left_edge)
        # cv.createTrackbar("bright_top_left_edge", "image", 190, 255, self.update_bright_top_left_edge)
        # cv.createTrackbar("bright_top_right_edge", "image", 200, 255, self.update_bright_top_right_edge)
        # cv.createTrackbar("bright_down_right_edge", "image", 230, 255, self.update_bright_down_right_edge)
        # cv.createTrackbar("brighter_top_right_edge", "image", 220, 255, self.update_brighter_down_left_edge)
        # cv.createTrackbar("brighter_down_right_edge", "image", 240, 255, self.update_brighter_top_left_edge)
        self.update_image()

        hist = cv.calcHist([self.src_image], [0], None, [256], [0, 256])
        plt.subplot(221)
        plt.plot(hist, color= 'r')
        plt.xlim([0, 256])
        plt.subplot(222)
        plt.imshow(self.src_image, cmap='gray')
        plt.show()

        cv.waitKey(0)
        cv.destroyAllWindows()


    def update_darker_top_right_edge(self, val):
        dark_top_edge = val
        self.update_image()

    def update_darker_down_right_edge(self, val):
        dark_down_edge = val
        self.update_image()

    def update_dark_down_left_edge(self, val):
        gray_left_edge = val
        self.update_image()

    def update_dark_top_left_edge(self, val):
        gray_top_edge = val
        self.update_image()

    def update_dark_top_right_edge(self, val):
        gray_right_edge = val
        self.update_image()

    def update_dark_down_right_edge(self, val):
        bright_top_edge = val
        self.update_image()

    def update_gray_down_left_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_gray_top_left_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_gray_top_right_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_gray_down_right_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_bright_down_left_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_bright_top_left_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_bright_top_right_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_bright_down_right_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_brighter_down_left_edge(self, val):
        bright_down_edge = val
        self.update_image()

    def update_brighter_top_left_edge(self, val):
        bright_down_edge = val
        self.update_image()


    def update_image(self):
        for i in range(0, len(self.src_image)):
            for j in range(0, len(self.src_image[0])):
                gray = self.update_contrast(self.src_image[i][j])
                self.src_image[i][j] = gray
        # cv.imshow('window_image', self.src_image)


    def update_contrast(self, gray):
        darker_value = 0
        if gray <= self.darker_top_right_edge:
            darker_value = 1
        elif gray > self.darker_top_right_edge and gray <= self.darker_down_right_edge:
            darker_value = self.get_value(self.darker_top_right_edge, self.darker_down_right_edge, 1, 0, gray)

        dark_value = 0
        if gray >= self.dark_down_left_edge and gray <= self.dark_top_left_edge:
            dark_value = self.get_value(self.dark_down_left_edge, self.dark_top_left_edge, 0, 1, gray)
        elif gray >= self.dark_top_left_edge and gray <= self.dark_top_right_edge:
            dark_value = 1
        elif gray >= self.dark_top_right_edge and gray < self.dark_down_right_edge:
            dark_value = self.get_value(self.dark_top_right_edge, self.dark_down_right_edge, 1, 0, gray)

        gray_value = 0
        if gray >= self.gray_down_left_edge and gray <= self.gray_top_left_edge:
            gray_value = self.get_value(self.gray_down_left_edge, self.gray_top_left_edge, 0, 1, gray)
        elif gray >= self.gray_top_left_edge and gray <= self.gray_top_right_edge:
            gray_value = 1
        if gray >= self.gray_top_right_edge and gray <= self.gray_down_right_edge:
            gray_value = self.get_value(self.gray_top_right_edge, self.gray_down_right_edge, 1, 0, gray)

        bright_value = 0
        if gray >= self.bright_down_left_edge and gray <= self.bright_top_left_edge:
            bright_value = self.get_value(self.bright_down_left_edge, self.bright_top_left_edge, 0, 1, gray)
        elif gray >= self.bright_top_left_edge and gray <= self.bright_top_right_edge:
            bright_value = 1
        if gray >= self.bright_top_right_edge and gray <= self.bright_down_right_edge:
            bright_value = self.get_value(self.bright_top_right_edge, self.bright_down_right_edge, 1, 0, gray)

        brighter_value = 0
        if gray > self.brighter_down_left_edge and gray <= self.brighter_top_left_edge:
            brighter_value = self.get_value(self.brighter_down_left_edge, self.brighter_top_left_edge, 0, 1, gray)
        elif gray >= self.brighter_top_left_edge:
            brighter_value = 1

        value = (
                self.DARKER_CONST * darker_value + self.DARK_CONST * dark_value + self.GRAY_CONST * gray_value + self.BRIGHT_CONST * bright_value + self.BRIGHTER_CONST * brighter_value) / (
                darker_value + dark_value + gray_value + bright_value + brighter_value)
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

