'''
This file is created by Yuyu Qian, Computer Science and Technology Department, Zhejiang University
qianyuyulys@gmail.com
This code could be used for any non-commercial purpose. You can edit and reconstruct it. When you use this code please
cite the author.
'''

import numpy as np
import random
import matplotlib.pyplot as plt

def generate_dataList(scaleX = 2.0, scaleY = 0.8):
    dataList = []
    x = []
    y = []
    for i in range(2000):
        temp = random.random()
        x.append(temp*scaleX*np.pi)
        sin_part = np.sin(temp * scaleX * np.pi) + scaleY * random.random() - (scaleY / 0.5)
        cos_part = np.cos(temp * scaleX/100.0 * np.pi) + (scaleY/3.0) * random.random() - ((scaleY/3.0) / 0.5)
        y.append(sin_part + cos_part)

    print(x,y)
    plt.plot(x, y, c='xkcd:orange', marker='o', ls='None')
    # red_patch = mpatches.Patch(color='xkcd:baby poop green', label='Order 7 Polynomial')
    # plt.legend(handles=[red_patch])
    # plt.show()
    return [x, y]

# def Hessenberg(polinomial_order_you_expect):
#     J = Jacobian(polinomial_order_you_expect)
#
# def least_sqaure(dataList, polinomial_parameter_list):
#     pass
#
# def Levenberg_Marquardt(data_list, polinomial_order_you_expect):
#     J = Jacobian(polinomial_order_you_expect)

def Hypothesis(xList, parameters):
    H = []
    for x in xList:
        Polinomial_result = 0.0
        for order, parameter in enumerate(parameters):
            Polinomial_result += (float(parameter)*float(x)**order)
        H.append(Polinomial_result)
    # ##########
    # print("The hypothesis y are:", H)
    # ##########
    return H

def Hypothesis_Offset(dataList, parameters):
    '''
    dataList = [2][n]  dataList[0] = xList dataList[1] = yList 
    
    F = Hypothesis - yList
    
    :param dataList: 
    :return: 
    '''

    H = Hypothesis(dataList[0], parameters)
    F = [Hy-float(Ry) for Hy, Ry in zip(H, dataList[1])]
    # ##########
    # print("The real y are:", dataList[1])
    # print("The delta are F:", F)
    # ##########
    return np.asarray(F)

def Jacobian(xList, parameters):
    J = []
    for x in xList:
        row = []
        for order, parameter in enumerate(parameters):
            row.append(x**order)
        J.append(row)
    # ##########
    # print('Jacobian:', J)
    # ##########
    return np.asarray(J)

def delta_para(dataList, parameters):
    J = Jacobian(dataList[0], parameters)
    F = Hypothesis_Offset(dataList, parameters)
    a = np.matmul(np.transpose(J), np.transpose(F))
    b = np.matmul(np.transpose(J), J)

    ##########
    # print(a)
    # print(b)
    ##########

    p = np.linalg.solve(b, np.negative(a))
    print('parameter_delta:', p)
    return p

def draw_hypothesis(parameters, color_cmap, cmap, scaleX = 2.0, scaleY = 0.8):
    xList = []
    yList = []
    for x in np.arange(0.0, scaleX*np.pi, scaleX*np.pi/1000):
        xList.append(x)
        y = 0.0
        for order, parameter in enumerate(parameters):
            y += (parameter*x**order)
        yList.append(y)
    plt.plot(xList, yList, c=cmap(color_cmap), marker='*', ls='-')



def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def main():


    # Hypothesis([1., 2., 3.], [2, 3, 3])
    parameters = [2,3,3]
    # data_list = [[1,2,3,4,5],[2,3,4,5,6]]
    # Hypothesis_Offset(data_list, parameters)
    # Jacobian(data_list[0], parameters)

    scaleX = 4.0
    scaleY = 0.8
    data_list = generate_dataList(scaleX, scaleY)
    parameters = [1, 0.5, 1, 1, 1, 1, 1]
    IterTime = 9
    cmap = get_cmap(IterTime)
    plt.figure(1)
    for i in range(IterTime):
        p = delta_para(data_list, parameters)
        parameters = [pk+p_delta for pk, p_delta in zip(parameters, p)]
        if (i % 1) == 0:
            draw_hypothesis(parameters, i, cmap, scaleX, scaleY)
    plt.show()

    # tt = [1, 2, 4, 5, 8]
    # yy = [3.2939, 4.2699, 7.1749, 9.3008, 20.259]
    # F = []
    # for t,y in zip(tt, yy):
    #     ans = 2.5*np.exp(0.25*t)
    #     least_sqaure = 0.5 * (y-ans)**0.5
    #     F.append(ans-y)
    #
    #     # ans_list.append(ans)
    #     print("Hypothesis:", ans, end=' ')
    #     print("Least Square:", least_sqaure )

if __name__ == '__main__':
    main()

