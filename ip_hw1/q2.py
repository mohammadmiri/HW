import numpy, matplotlib.pyplot as plt
from scipy import misc


def main():
    mu, sigma = 0, 5
    number = int(input())
    image = misc.imread('34.png')
    images = add_noise(image, mu, sigma, number)
    new_image = average(images, image)
    subtract_image = subtract(image1=image, image2=new_image)
    # show original image
    plt.figure()
    plt.imshow(image)
    plt.title('original image')
    plt.show()
    # show averaged image
    plt.figure()
    plt.imshow(new_image)
    plt.title('averaged image')
    plt.show()
    # show subtract image
    plt.figure()
    plt.title('sub image')
    plt.imshow(subtract_image)
    plt.show()
    # show histogram
    plt.figure()
    plt.title('histogram')
    plt.hist(subtract_image.flat)
    plt.show()
    # show noisy images
    for image in images:
        plt.figure()
        plt.title('noisy image')
        plt.imshow(image)
        plt.show()
    input()


def average(images, image):
    copy_image = numpy.zeros(shape=(len(image), len(image[0])))
    for i in range(0, len(copy_image)):
        for j in range(0, len(copy_image[i])):
            for n in range(0, len(images)):
                copy_image[i][j] += images[n][i][j]
            copy_image[i][j] /= len(images)
    return copy_image.astype(int)


def add_noise(image, mu, sigma, number):
    images = []
    for n in range(0, number):
        s = numpy.random.normal(mu, sigma, image.size)
        # add noise to image
        t = 0
        temp_image = image.astype(float)
        for i in range(0, len(temp_image)):
            for j in range(0, len(temp_image[i])):
                temp_image += s[t]
                t += 1
        images.append(temp_image)
    return images


def subtract(image1, image2):
    sub = numpy.zeros((len(image1), len(image1[0])))
    for i in range(0, len(image1)):
        for j in range(0, len(image1[i])):
            sub[i][j] = scale(image1[i][j] - image2[i][j], max=510, min=0)
    return sub


def scale(number, max, min):
    return (number - min) * 255 / (max - min)


main()
