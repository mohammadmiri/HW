import matplotlib.pyplot as plt
from scipy import misc
import numpy
import os

import cv2


def main():
    dir = os.path.dirname(__file__)

    source_image = misc.imread(dir+'/gs.jpg')
    source_image_hist = get_histogram(source_image)
    source_image_pdf = get_pdf(source_image_hist)
    source_image_cdf = get_cdf(source_image_pdf, 255)

    target_image = convert_to_grayscale(misc.imread(dir+'/2.png'))
    target_image_hist = get_histogram(target_image)
    target_image_pdf = get_pdf(target_image_hist)
    target_image_cdf = get_cdf(target_image_pdf, 255)

    map_gray = specify(source_image_cdf, target_image_cdf)
    result_image = convert_to_specified(source_image, map_gray)
    plt.hist(result_image.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.show()

    res = numpy.hstack((result_image, source_image))
    cv2.imwrite(dir+'/res.png', res)


def convert_to_grayscale(image):
    converted_image = numpy.zeros(shape=(len(image), len((image[0])))).astype(int)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            converted_image[i][j] = int(image[i][j][0])
    return converted_image


def get_histogram(image):
    hist = numpy.zeros(256)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            hist[image[i][j]] += 1
    return hist


def get_pdf(hist):
    total = 0
    for i in hist:
        total += i
    pdf = numpy.zeros(256).astype(float)
    for i in range(0, len(hist)):
        pdf[i] = float(hist[i]/total)
    return pdf


def get_cdf(pdf, level):
    temp = 0
    cdf = numpy.zeros(256).astype(int)
    for i in range(0, len(pdf)):
        temp += pdf[i]
        cdf[i] = round(level*temp)
    return cdf


def specify(source_cdf, target_cdf):
    result = numpy.zeros(256).astype(int)
    for i in range(0, len(target_cdf)):
        cdf = target_cdf[i]
        for j in range(0, len(source_cdf)):
            if cdf <= source_cdf[j]:
                result[i] = j
                break
    return result


def convert_to_specified(source_img, map_gray):
    new_image = numpy.empty_like(source_img)
    for i in range(0, len(new_image)):
        for j in range(0, len(new_image[i])):
            gray_scale = map_gray[source_img[i][j]]
            new_image[i][j] = gray_scale
    return new_image


main()
