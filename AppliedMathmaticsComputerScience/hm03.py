# -*- coding:utf-8 -*-
'''
This file is created by Yuyu Qian, Computer Science and Technology Department, Zhejiang University
qianyuyulys@gmail.com
This code could be used for any non-commercial purpose. You can edit and reconstruct it. When you use this code please
cite the author.
'''
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats
# import scipy.interpolate
import random
from matplotlib import ticker, cm

def Gaussian_Distribution_2D_Generate(num1 = 200, Fisrt_x0 = 0, First_y0 = 0, sigma1x = 1, sigma1y = 2, num2 = 300,  Second_x0 = 5, Second_y0 = 7, sigma2x = 3, sigma2y = 4):
    x = []
    y = []
    for i in range(num1):
        x.append(sigma1x * np.random.randn() + Fisrt_x0)
        y.append(sigma1y * np.random.randn() + First_y0)

    xx = []
    yy = []
    for i in range(num2):
        xx.append(sigma2x * np.random.randn() + Second_x0)
        yy.append(sigma2y * np.random.randn() + Second_y0)

    plt.figure(1)
    plt.plot(xx, yy, c='blue', marker='*', ls='None')
    plt.plot(x, y, c='red', marker='+', ls='None')
    plt.show()

    return x, y, xx, yy

def calculate_probability(sample, mean, sigma):
    return (1 / (np.sqrt(2*np.pi)*sigma)) * np.e**(-(((sample-mean)**2)/(2*sigma**2)))

def calculate_probability_v2(x, y, mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair):
    rho = 0
    temp0 = -1/(2*(1-rho**2))
    temp1 = ((x-mean_x_pair[0])**2/sigma_x_pair[0]**2)
    temp2 = ((y-mean_y_pair[0])**2/sigma_y_pair[0]**2)
    temp3 = 2*rho*(x - mean_x_pair[0])*(y-mean_y_pair[0])/(sigma_x_pair[0]*sigma_y_pair[0])
    temp4 = 1/(2*np.pi*sigma_x_pair[0]*sigma_y_pair[0]*np.sqrt(1-rho**2))
    probability1 = temp4*np.e**(temp0*(temp1+temp2-temp3))

    temp0 = -1/(2*(1-rho**2))
    temp1 = ((x-mean_x_pair[1])**2)/(sigma_x_pair[1]**2)
    temp2 = ((y-mean_y_pair[1])**2)/(sigma_y_pair[1]**2)
    temp3 = 2*rho*(x - mean_x_pair[1])*(y-mean_y_pair[1])/(sigma_x_pair[1]*sigma_y_pair[1])
    temp4 = 1/(2*np.pi*sigma_x_pair[1]*sigma_y_pair[1]*np.sqrt(1-rho**2))
    probability2 = temp4*np.e**(temp0*(temp1+temp2-temp3))
    return probability1, probability2

def divide(list, mean_list=[0, 0], sigma_list=[1, 1], num_of_class=2):
    list1 = []
    list2 = []
    for sample in list:
        p_1 = calculate_probability(sample, mean_list[0], sigma_list[0])
        p_2 = calculate_probability(sample, mean_list[1], sigma_list[1])
        if p_1 >= p_2:
            list1.append(sample)
        else:
            list2.append(sample)
    return list1, list2

def divide_2(data_x_list, data_y_list, mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair):
    listX1 = []
    listX2 = []
    listY1 = []
    listY2 = []
    for x, y in zip(data_x_list, data_y_list):
        p_1, p_2= calculate_probability_v2(x, y, mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair)
        # p_2 = calculate_probability_v2(x, y, mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair)
        if p_1 >= p_2:
            listX1.append(x)
            listY1.append(y)
        else:
            listX2.append(x)
            listY2.append(y)
    return listX1, listX2, listY1, listY2

def calculate_mean(list):
    sum = 0.0
    for sample in list:
        sum += sample
    mean = sum / len(list)
    return mean

def calculate_simga(list, mean):
    sum = 0.0
    for sample in list:
        sum += ((sample-mean)**2)
    sigma = np.sqrt(sum / len(list))
    return sigma

def confidence_interval():
    pass
# need to be improved, the draw range is not correct
def draw(mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair, figureName=1):

    # fun_x_1 =lambda sample: (1 / (np.sqrt(2*np.pi)*sigma_x_pair[0])) * np.e**(-(((sample-mean_x_pair[0])**2)/(2*sigma_x_pair[0]**2)))
    confidence = 0.95
    h = sigma_x_pair[0] * sp.stats.norm.ppf((1 + confidence) / 2.)
    x_1_min = mean_x_pair[0] - h
    x_1_max = mean_x_pair[0] + h

    # fun_y_1 =lambda sample: (1 / (np.sqrt(2*np.pi)*sigma_y_pair[0])) * np.e**(-(((sample-mean_y_pair[0])**2)/(2*sigma_y_pair[0]**2)))
    confidence = 0.95
    h = sigma_y_pair[0] * sp.stats.norm.ppf((1 + confidence) / 2.)
    y_1_min = mean_y_pair[0] - h
    y_1_max = mean_y_pair[0] + h

    # fun_x_2 = lambda sample: (1 / (np.sqrt(2 * np.pi) * sigma_x_pair[1])) * np.e ** (-(((sample - mean_x_pair[1]) ** 2) / (2 * sigma_x_pair[1] ** 2)))
    confidence = 0.95
    h = sigma_x_pair[1] * sp.stats.norm.ppf((1 + confidence) / 2.)
    x_2_min = mean_x_pair[1] - h
    x_2_max = mean_x_pair[1] + h

    # fun_y_2 = lambda sample: (1 / (np.sqrt(2 * np.pi) * sigma_y_pair[1])) * np.e ** (-(((sample - mean_y_pair[1]) ** 2) / (2 * sigma_y_pair[1] ** 2)))
    confidence = 0.95
    h = sigma_y_pair[1] * sp.stats.norm.ppf((1 + confidence) / 2.)
    y_2_min = mean_y_pair[1] - h
    y_2_max = mean_y_pair[1] + h

    N = 1000
    delta = 0.01
    x1 = np.linspace(x_1_min, x_1_max, N)
    y1 = np.linspace(y_1_min, y_1_max, N)
    X1, Y1 = np.meshgrid(x1, y1)
    XX1 = np.arange(-4.1, 16.1, delta)
    YY1 = np.arange(-4.1, 16.1, delta)
    meshX1, meshY1 = np.meshgrid(XX1, YY1)

    x2 = np.linspace(x_2_min, x_2_max, N)
    y2 = np.linspace(y_2_min, y_2_max, N)
    X2, Y2 = np.meshgrid(x2, y2)

    rho = 0
    temp0 = -1/(2*(1-rho**2))
    temp1 = ((X1-mean_x_pair[0])**2/sigma_x_pair[0]**2)
    temp2 = ((Y1-mean_y_pair[0])**2/sigma_y_pair[0]**2)
    temp3 = 2*rho*(X1 - mean_x_pair[0])*(Y1-mean_y_pair[0])/(sigma_x_pair[0]*sigma_y_pair[0])
    temp4 = 1/(2*np.pi*sigma_x_pair[0]*sigma_y_pair[0]*np.sqrt(1-rho**2))
    Z1 = temp4*np.e**(temp0*(temp1+temp2-temp3))
    temp5 = ((X1*10-mean_x_pair[0])**2/sigma_x_pair[0]**2)
    temp6 = ((Y1*10-mean_y_pair[0])**2/sigma_y_pair[0]**2)
    ZZ1 = temp4 * np.e ** (temp0 * (temp5 + temp6 - temp3))
    z1 = Z1 + 50 * ZZ1
    # fig, ax = plt.subplots()

    temp0 = -1/(2*(1-rho**2))
    temp1 = ((X2-mean_x_pair[1])**2/sigma_x_pair[1]**2)
    temp2 = ((Y2-mean_y_pair[1])**2/sigma_y_pair[1]**2)
    temp3 = 2*rho*(X1 - mean_x_pair[1])*(Y1-mean_y_pair[1])/(sigma_x_pair[1]*sigma_y_pair[1])
    temp4 = 1/(2*np.pi*sigma_x_pair[1]*sigma_y_pair[1]*np.sqrt(1-rho**2))
    Z2 = temp4*np.e**(temp0*(temp1+temp2-temp3))
    temp5 = ((X1*10-mean_x_pair[1])**2/sigma_x_pair[1]**2)
    temp6 = ((Y1*10-mean_y_pair[1])**2/sigma_y_pair[1]**2)
    ZZ2 = temp4 * np.e ** (temp0 * (temp5 + temp6 - temp3))
    z2 = Z2 + 50 * ZZ2
    fig, ax = plt.subplots()
    cs1 = ax.contourf(X1, Y1, z1, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
    cs2 = ax.contourf(X2, Y2, z2, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
    cbar1 = fig.colorbar(cs1)
    # cbar2 = fig.colorbar(cs2)
    plt.show()
    # plt.figure(figureName)

def draw_v2():
    def gaussian_2d(x, y, x0, y0, xsig, ysig):
        return np.exp(-0.5 * (((x - x0) / xsig) ** 2 + ((y - y0) / ysig) ** 2))

    delta = 0.025
    x = np.arange(-3.0, 10.0, delta)
    y = np.arange(-3.0, 10.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = gaussian_2d(X, Y, 0., 0., 1., 1.)
    Z2 = gaussian_2d(X, Y, 1., 1., 1.5, 0.5)
    # difference of Gaussians
    Z = 10.0 * (Z2 - Z1)

    # Create a contour plot with labels using default colors.  The
    # inline argument to clabel will control whether the labels are draw
    # over the line segments of the contour, removing the lines beneath
    # the label
    plt.clf()
    CS = plt.contour(X, Y, Z)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Simplest default with labels')

def plot_countour(x,y,z, npts):
    # plt.figure(3)
    # define grid.
    xi = np.linspace(-4.1, 16.1, 3000)
    yi = np.linspace(-4.1, 16.1, 3000)
    ## grid the data.
    zi = sp.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')
    levels = [0.005, 0.01, 0.1, 0.2, 0.4, 1.0]
    # levels = [1.0, 0.8, 0.4, 0.2, 0.1, 0.005]
    # contour the gridded data, plotting dots at the randomly spaced data points.
    CS = plt.contour(xi,yi,zi,len(levels), linewidths=0.5, colors='orange', levels=levels, alpha=0.5)
    #CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet)
    cmap = plt.cm.get_cmap("winter")
    cmap.set_under("magenta")
    cmap.set_over("yellow")
    CS = plt.contourf(xi,yi,zi,len(levels), cmap=cmap, levels=levels)
    plt.colorbar() # draw colorbar
    # plot data points.
    # plt.scatter(x, y, marker='o', c='b', s=5)
    plt.xlim(-4, 16)
    plt.ylim(-4, 16)
    plt.title('Gaussian_2D')

def gaussian_2d(x, y, x0, y0, xsig, ysig):
    return np.exp(-0.5*(((x-x0) / xsig)**2 + ((y-y0) / ysig)**2))

def E_M(data_x_list, data_y_list, x1_list, y1_list, x2_list, y2_list, Step, \
        mean_x_pair=[0., 4.], sigma_x_pair=[1., 1.], mean_y_pair=[0., 4.], sigma_y_pair=[1., 1.]):
    plt.clf()
    plt.plot(data_x_list, data_y_list, c='purple', marker='*', ls='None')
    # draw(mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair, figureName=1)
    delta = 0.01
    x = np.arange(-4.1, 16.1, delta)
    y = np.arange(-4.1, 16.1, delta)
    z = gauss(x1_list, y1_list, Sigma=np.asarray([[sigma_x_pair[0], 0.5], [0.5, sigma_y_pair[0]]]), mu=np.asarray([mean_x_pair[0], mean_y_pair[0]]))
    plot_countour(x1_list, y1_list, z, 1000)
    # plt.show()
    zz = gauss(x2_list, y2_list, Sigma=np.asarray([[sigma_x_pair[1], 0.5], [0.5, sigma_y_pair[1]]]), mu=np.asarray([mean_x_pair[1], mean_y_pair[1]]))
    plot_countour(x2_list, y2_list, zz, 1000)
    plt.show()
    if (Step % 1)==0:
        plt.savefig('Step_%s.jpg' % str(Step))
    # draw(mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair)

    # Expectation Method for the Input Data
    # divide should divide data with 2 dimension together !
    # listX1, listX2 = divide(data_x_list, mean_x_pair, sigma_x_pair)
    # listY1, listY2 = divide(data_y_list, mean_y_pair, sigma_y_pair)
    listX1, listX2, listY1, listY2 = divide_2(data_x_list, data_y_list, mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair)

    # ML Method for the New Sets of Data
    mean_x_pair[0] = calculate_mean(listX1)
    mean_x_pair[1] = calculate_mean(listX2)
    mean_y_pair[0] = calculate_mean(listY1)
    mean_y_pair[1] = calculate_mean(listY2)
    sigma_x_pair[0] = calculate_simga(listX1, mean_x_pair[0])
    sigma_x_pair[1] = calculate_simga(listX2, mean_x_pair[1])
    sigma_y_pair[0] = calculate_simga(listY1, mean_y_pair[0])
    sigma_y_pair[1] = calculate_simga(listY2, mean_y_pair[1])

    ############ Test
    # z = gauss(listX1, listY1, Sigma=np.asarray([[sigma_x_pair[0], .5], [0.5, sigma_y_pair[0]]]), mu=np.asarray([mean_x_pair[0], mean_y_pair[0]]))
    # plot_countour(listX1, listY1, z, 1000)
    # # plt.show()
    # zz = gauss(listX2, listY2, Sigma=np.asarray([[sigma_x_pair[1], .5], [0.5, sigma_y_pair[1]]]), mu=np.asarray([mean_x_pair[1], mean_y_pair[1]]))
    # plot_countour(listX2, listY2, zz, 1000)
    # plt.show()
    ############

    return mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair

def gauss(x,y,Sigma,mu):
    X=np.vstack((x,y)).T
    mat_multi=np.dot((X-mu[None,...]).dot(np.linalg.inv(Sigma)),(X-mu[None,...]).T)
    return  np.diag(np.exp(-1*(mat_multi)))

def main():
    x1_list, y1_list, x2_list, y2_list = Gaussian_Distribution_2D_Generate()
    data_x_list = []
    data_y_list = []
    data_x_list.extend(x1_list)
    data_x_list.extend(x2_list)
    data_y_list.extend(y1_list)
    data_y_list.extend(y2_list)
    plt.figure(2)
    plt.plot(data_x_list, data_y_list, c='purple', marker='*', ls='None')
    plt.show()
    mean_x_pair = [0.1, 6.]
    sigma_x_pair = [1., 1.2]
    mean_y_pair = [5., 4.1]
    sigma_y_pair = [1., 1.2]
    for Step in range(4):
        mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair = E_M(data_x_list, data_y_list, x1_list, y1_list, x2_list, y2_list, Step, mean_x_pair, sigma_x_pair, mean_y_pair, sigma_y_pair)
    # print(calculate_probability_v2(-0.1, -0.1, [0., 1.], [.2, .4], [0., 1.], [.2, .4]))


if __name__ == '__main__':
    main()