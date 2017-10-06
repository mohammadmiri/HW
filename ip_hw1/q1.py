import matplotlib.pyplot as plt
from scipy import misc
import numpy
import math

def main():
    # file_name = str(input())
    magnify = 1+int(input())/100
    image = misc.imread('image2.png')
    new_image_size = (int(len(image)*magnify), int(len(image[0])*magnify))
    image_resized_ni = nearest_interpolate(image, new_image_size, magnify)
    image_resized_bi = bilinear_interpolate(image, new_image_size, magnify)


    plt.figure()
    plt.imshow(image)
    plt.figure()
    plt.imshow(image_resized_ni)
    plt.figure()
    plt.imshow(image_resized_bi)
    plt.show()


def show_image(image):
    plt.imshow(image)
    plt.show()


def nearest_interpolate(image, new_image_size, magnify):
    new_image = numpy.zeros(new_image_size)
    for i in range(0, len(new_image)):
        for j in range(0, len(new_image[i])):
            # call for get vertical position
            x = get_nearest(i, magnify)
            # call for get horizontal position
            y = get_nearest(j, magnify)
            new_image[i][j] = image[x][y]
    return new_image


# get new position of magnified pixel in one dimension
def get_nearest(new_pixel, magnify):
    return int(round(new_pixel / magnify))


def bilinear_interpolate(image, new_image_size, magnify):
    new_image = numpy.zeros(new_image_size)
    for i in range(0, len(new_image)):
        for j in range(0, len(new_image[i])):
            center = get_center(i, j, magnify)
            gray = 0
            points = find_four_neighborhood(get_nearest(i, magnify), get_nearest(j, magnify), center)
            gray += math.fabs(center['i'] - get_center(points[0]['i'], points[0]['j'], 1)['i'])\
                    * math.fabs(center['j'] - get_center(points[0]['i'], points[0]['j'], 1)['j'])\
                    * get_gray(points[0]['i'], points[0]['j'], image)
            gray += math.fabs(center['i'] - get_center(points[1]['i'], points[1]['j'], 1)['i']) \
                    * math.fabs(center['j'] - get_center(points[1]['i'], points[1]['j'], 1)['j'])\
                    * get_gray(points[1]['i'], points[1]['j'], image)
            gray += math.fabs(center['i'] - get_center(points[2]['i'], points[2]['j'], 1)['i']) \
                    * math.fabs(center['j'] - get_center(points[2]['i'], points[2]['j'], 1)['j'])\
                    * get_gray(points[0]['i'], points[0]['j'], image)
            gray += math.fabs(center['i'] - get_center(points[3]['i'], points[3]['j'], 1)['i']) \
                    * math.fabs(center['j'] - get_center(points[3]['i'], points[3]['j'], 1)['j']) \
                    * get_gray(points[0]['i'], points[0]['j'], image)
            new_image[i][j] = gray
    return new_image


def get_gray(i, j, image):
    try:
        return image[i][j]
    except:
        return 0


# finding four points
def find_four_neighborhood(i, j, center):
    p1 = {'i':i, 'j':j}
    if center['j'] > j+0.5:
        p2 = {'i':i, 'j':j+1}
        if center['i'] > i+0.5:
            p3 = {'i': i + 1, 'j': j}
            p4 = {'i': i + 1, 'j': j + 1}
        else:
            p3 = {'i': i - 1, 'j': j}
            p4 = {'i': i - 1, 'j': j + 1}
    else:
        p2 = {'i': i, 'j': j - 1}
        if center['i'] > i + 0.5:
            p3 = {'i': i + 1, 'j': j}
            p4 = {'i': i + 1, 'j': j - 1}
        else:
            p3 = {'i': i - 1, 'j': j}
            p4 = {'i': i - 1, 'j': j - 1}
    return [p1, p2, p3, p4]


def get_center(i, j, magnify=1):
    return {'i':(i+0.5)/magnify , 'j':(j+0.5)/magnify}


main()


