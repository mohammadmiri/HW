import matplotlib.pyplot as plt, numpy
from matplotlib.colors import LogNorm
import math


SIGMA_POINT1_X = math.sqrt(5)
SIGMA_POINT1_Y = math.sqrt(5)
SIGMA_POINT2_X = math.sqrt(5)
SIGMA_POINT2_Y = math.sqrt(5)
MU_POINT1_X = 10
MU_POINT1_Y = 10
MU_POINT2_X = 20
MU_POINT2_Y = 20

points_number = 100

def main():
    point1_Xs = numpy.random.normal(MU_POINT1_X, SIGMA_POINT1_X, points_number).astype(int)
    point2_Xs = numpy.random.normal(MU_POINT2_X, SIGMA_POINT2_X, points_number).astype(int)
    point1_Ys = numpy.random.normal(MU_POINT1_Y, SIGMA_POINT1_Y, points_number).astype(int)
    point2_Ys = numpy.random.normal(MU_POINT2_Y, SIGMA_POINT2_Y, points_number).astype(int)

    mu1_x = get_mean(point1_Xs)
    mu1_y = get_mean(point1_Ys)
    mu2_x = get_mean(point2_Xs)
    mu2_y = get_mean(point2_Ys)

    var1_x = get_variance(point1_Xs, mu1_x)
    var1_y = get_variance(point1_Ys, mu1_y)
    var2_x = get_variance(point2_Xs, mu2_x)
    var2_y = get_variance(point2_Ys, mu2_y)


    plt.hist2d(numpy.concatenate([point1_Xs,point2_Xs]), numpy.concatenate([point1_Ys,point2_Ys]), normed=LogNorm)
    plt.colorbar()
    plt.show()


def get_mean(points):
    s = 0
    for x in points:
        s += x
    return s/len(points)


def get_variance(points, mean):
    s = 0
    for x in points:
        s += math.pow(x-mean, 2)
    return s/len(points)


main()
