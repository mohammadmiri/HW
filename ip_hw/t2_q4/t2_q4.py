import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy

mask3 = [[0,1,0],
        [1,-4,1],
        [0,1,0]]

mask5 = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]


class ImageTransformer:

    def __init__(self):
        self.threshold = 127
        self.src_image = None
        self.dst_image = None


    def main(self):
        dir = os.path.dirname(__file__)
        self.src_image = cv.imread(dir + '/gs.jpg', 0)
        self.dst_image = numpy.empty_like(self.src_image)
        cv.imshow("image", self.dst_image)
        cv.namedWindow("image", 0)
        cv.createTrackbar("threshold", "image", 127, 255, self.update_threshold)
        self.update_image()

        result = self.apply_mask(mask=mask3, image=self.src_image)
        plt.subplot(221)
        plt.imshow(result, cmap='gray')
        plt.subplot(222)
        plt.imshow(self.src_image, cmap='gray')
        plt.show()

        cv.waitKey(0)
        cv.destroyAllWindows()


    def update_threshold(self, val):
        self.threshold = val
        self.update_image()


    def update_image(self):
        for i in range(0, len(self.src_image)):
            for j in range(0, len(self.src_image[0])):
                if self.src_image[i][j] <= self.threshold:
                    self.dst_image[i][j] = 0
                else:
                    self.dst_image[i][j] = 255
        cv.imshow('image', self.dst_image)


    def apply_mask(self, mask, image):
        result = numpy.zeros(shape=(len(image), len(image[0])))
        a = int((len(mask)-1)/2)
        b = int((len(mask[0])-1)/2)
        for i in range(a, len(image)-a):
            for j in range(b, len(image[i])-b):
                for s in range(-a, a+1):
                    for t in range(-b, b+1):
                        result[i][j] += image[i + s][j + t] * mask[s][t]
        return result


if __name__ == '__main__':
    obj = ImageTransformer()
    obj.main()
