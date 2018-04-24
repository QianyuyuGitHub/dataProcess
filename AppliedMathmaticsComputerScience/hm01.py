# -*- coding:utf-8 -*-
'''
This file is created by Yuyu Qian, Computer Science and Technology Department, Zhejiang University
qianyuyulys@gmail.com
This code could be used for any non-commercial purpose. You can edit and reconstruct it. When you use this code please
cite the author.
'''
import numpy
# import TensorFlow as tf
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches

def curveFitting(order, dataList, valve=0.1, step=0.05, displayStep=20):
    parameter = []
    xList = []
    yList = []
    sum = 0
    grad = []  # a list to store all the gradient decent of m dimensions factors
    t1 = numpy.arange(-1.0, 1.0, 0.2)
    t2 = numpy.arange(-1.0, 1.0, 0.02)
    plt.figure(1)
    plt.subplot(211)
    for x, y in dataList:
        xList.append(x)
        yList.append(y)
    distance = 10.0 ** 6
    print('The initial polynomial is:', end='')
    for i in range(order + 1):
        parameter.append(0)  # initialize all the factors
        grad.append(0)
        print(parameter[i], 'x^(', i, ')', end=' ')
    count = 0
    while distance >= valve and count != 1001:
        for k in range(len(dataList)):  # this loop is for all the points x in dataList
            x = dataList[k][0]
            y = dataList[k][1]
            _y = 0
            for i in range(order + 1):  # this loop is the the polynomial y of one single point x
                _y += parameter[i] * (x ** i)
                grad[i] += (((_y - y) * x) / float(len(dataList)))  # this is the correspond gradient of factor[i]
                # you could update the factor here as well to get more frequent update
                # and then update the distance as well
                distance += ((_y - y) ** 2)
            for i in range(order + 1):
                parameter[i] = parameter[i] - step * grad[i]
        distance = distance / float(2.0 * len(dataList))

        def polynomial_fun(t):
            sum = []
            orderCount = 0
            for x in t:
                sum.append(0)
                for para in parameter:
                    sum[-1] += (para * (x ** orderCount))
                orderCount += 1
            return sum

        if (count % displayStep) == 0:
            print('\nThe current polynomial is:', end='')
            for i in range(order + 1):
                print(parameter[i], 'x^(', i, ')', end=' ')
        if count == 1000:
            plt.plot(t1, polynomial_fun(t1), 'bo', t2, polynomial_fun(t2), 'k')
        count += 1
    _y_final = []
    for x, y in dataList:
        orderCount = 0
        for para in parameter:
            sum += (para * (x ** orderCount))
        _y_final.append([sum])
    # def polynomial_fun(t):
    # 	sum = []
    # 	for x in t:
    # 		sum.append(0)
    # 		for para in parameter:
    # 			sum[-1] += (para * (x ** orderCount))
    # 	return sum

    # plt.plot(t1, polynomial_fun(t1), 'bo', t2, polynomial_fun(t2), 'k', t2, numpy.sin(2*numpy.pi*t2), 'r--')
    # plt.plot(xList, yList, 'g*', xList, _y_final, 'r*')
    # plt.plot(t1, np.sin(2*np.pi*t1), 'r--')
    plt.plot(t2, numpy.sin(2 * numpy.pi * t2), 'r--')
    plt.show()

def calculate_polynomial(factors, xList): # correct
    _y_list = []
    for x in xList:
        order = 0
        _y_list.append(0)
        for factor in factors:
            _y_list[-1] += factor * (x ** order)
            order += 1
    return _y_list

def distanceFunc(factors, xList, yList):
    distance = 0.0
    _y_list = calculate_polynomial(factors, xList)
    for x, y, _y in zip(xList, yList, _y_list):
        distance += ((_y - y) ** 2)
    return distance / (2 * len(xList))

def xList2Mat(xList, order):
    xListMat = []
    for x in xList:
        xListMat.append([])
        for i in range(order+1):
            xListMat[-1].append(x**(i))
    xListMat = numpy.array(xListMat)
    # xListMat = xListMat.transpose()
    # print("After the change, xList become:", xListMat)
    return xListMat

def gradient_decent(factors, xList, yList, order, distanceFunction, type=1, step=0.01):
    distance = distanceFunction(factors, xList, yList)
    # _y = 0
    print(factors)
    # if type == 1:
    # this type of updating will update the factor soon as
    # when get the correspondig gradient
    # orderCount_1 = 0
    # #################
    _yList = calculate_polynomial(factors, xList)
    grad = numpy.zeros(order + 1)
    xMat = xList2Mat(xList, order)
    _yList = numpy.array(_yList)
    yList = numpy.array(yList)
    loss = _yList - yList
    grad = numpy.dot(xMat, loss) / len(yList)
    print("grad:", grad)
    factors -= step * grad
    # print("After the gradient decent:", factors)

    # #################
    # for i in range(order + 1):  # clear the former data
    #     grad[i] = 0
    # grad = numpy.zeros(order+1)
    # #############
    # for x, y, _y in zip(xList, yList, _yList):
    #     ####
    #     # _y = 0  # clear the former data
    #     # for i in range(order + 1):  # this loop for traversing the factors
    #     #     _y += factors[i] * (x ** i)
    #     ####
    #
    #     # after traversing orders will you get the _y
    #     # the you can use it to calculate the grad
    #     for i in range(order + 1):  # grad can be parse into sum process
    #         grad[i] += (((_y - y) * (x ** i)) / len(xList))  # shoud devide here
    # #############
    # #############
    # for k in range(order + 1):
    #     # grad[k] /= len(xList)
    #     factors[k] -= step * grad[k]
    # distance = distanceFunction(factors, xList, yList)
    # #############
    # orderCount_1 += 1
    return factors, distance

def curveFittingSep(dataList, stop_offset=0.1, order=3):
    xList = []
    yList = []
    for x, y in dataList:
        xList.append(x)
        yList.append(y)
    distance = 10.0 ** 5
    # distanceLast = 0
    factors = numpy.zeros(order + 1)
    circleCount = 0
    while distance >= stop_offset:
        # distanceLast = distance
        factors, distance = gradient_decent(factors, xList, yList, order, distanceFunc, type=1, step=0.05)
        print(distance)
        if circleCount == 20:
            t1 = numpy.arange(-1.0, 1.0, 0.2)
            t2 = numpy.arange(-1.0, 1.0, 0.02)
            plt.figure(1)
            # plt.subplot(211)
            plt.plot(xList, calculate_polynomial(factors, xList), 'ko')
            plt.plot(xList, numpy.sin(xList), 'r--')
            plt.show()
            return 0
        circleCount += 1

def scan(dataList, order=3):
    pass

def geneData(variarent= 0.1, scale=0.01):
    dataList = []
    num = int((1.0/scale) + 1)
    randnSeed = variarent * numpy.random.randn(num) - variarent/2
    random.uniform(-variarent, variarent)
    dataCount = 0
    for a in numpy.arange(0.0, 1.0, 0.01):
        x = 2 * numpy.pi * a
        y = numpy.sin(x) + randnSeed[dataCount]
        dataList.append([x, y])
        dataCount += 1
    return dataList

def normalEquations(dataList, order=3):
    xList = []
    yList = []
    for x, y in dataList:
        xList.append(x)
        yList.append(y)
    yList = (numpy.asmatrix(yList)).transpose()
    xMat = xList2Mat(xList, order)
    print(xMat)
    xMatTrans = xMat.transpose()
    xTrans_x = numpy.matmul(xMatTrans, xMat)
    xTrans_x_inv = numpy.linalg.inv(xTrans_x)
    xTrans_x_inv_xTrans = xTrans_x = numpy.matmul(xTrans_x_inv, xMatTrans)
    thita = numpy.matmul(xTrans_x_inv_xTrans, yList)
    return thita

def main():
    dataList = geneData(variarent=0.3, scale=0.01)
    xList = []
    yList = []
    for x, y in dataList:
        xList.append(x)
        yList.append(y)
    # plt.figure(1)
    # plt.plot(xList, yList)



    order = 3
    plt.figure(1)
    # plt.subplot(211)
    print(xList)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    t = [2*numpy.pi*i for i in numpy.arange(-0.0, 1.0, 0.01)]
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    plt.plot(xList, yList, c='xkcd:purple', marker='o', ls='None')

    order = 5
    plt.figure(1)
    # plt.subplot(211)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    # plt.plot(xList, numpy.sin(xList), 'r*-')

    order = 7
    plt.figure(1)
    # plt.subplot(211)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    # plt.plot(xList, numpy.sin(xList), 'r*-')

    order = 9
    plt.figure(1)
    # plt.subplot(211)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    # plt.plot(xList, numpy.sin(xList), 'r*-')


    order = 3
    plt.figure(2)
    # plt.subplot(211)
    print(xList)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    t = [2 * numpy.pi * i for i in numpy.arange(-0.0, 1.0, 0.01)]
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    plt.plot(xList, yList, c='xkcd:violet', marker='o', ls='None')
    red_patch = mpatches.Patch(color='xkcd:violet', label='Order 3 Polynomial')
    plt.legend(handles=[red_patch])

    order = 5
    plt.figure(3)
    # plt.subplot(211)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    plt.plot(xList, yList, c='xkcd:pink', marker='o', ls='None')
    red_patch = mpatches.Patch(color='xkcd:pink', label='Order 5 Polynomial')
    plt.legend(handles=[red_patch])

    order = 7
    plt.figure(4)
    # plt.subplot(211)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    plt.plot(xList, yList, c='xkcd:baby poop green', marker='o', ls='None')
    red_patch = mpatches.Patch(color='xkcd:baby poop green', label='Order 7 Polynomial')
    plt.legend(handles=[red_patch])

    order = 9
    plt.figure(5)
    # plt.subplot(211)
    thita = normalEquations(dataList, order)
    print(thita)
    realThita = list(numpy.array(thita).reshape(-1, ))
    # this also good: numpy.array(thita).reshape(-1,).tolist()
    plt.plot(t, calculate_polynomial(realThita, t), label='$y = {i}th order Ploynomial(x)$'.format(i=order))
    plt.plot(xList, yList, c='xkcd:orange', marker='o', ls='None')
    red_patch = mpatches.Patch(color='orange', label='Order 9 Polynomial')
    plt.legend(handles=[red_patch])
    plt.show()

if __name__ == '__main__':
    main()
