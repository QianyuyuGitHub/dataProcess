'''
This file is created by Yuyu Qian, Computer Science and Technology Department, Zhejiang University
qianyuyulys@gmail.com
This code could be used for any non-commercial purpose. You can edit and reconstruct it. When you use this code please
cite the author.
'''

import numpy as np
import random
import matplotlib.pyplot as plt

def generate_dataList(dataNumber=300, xScale=2*np.pi, yScale=1):
    dataList1 = []
    dataList2 = []
    dataList = [[],[]]
    # xList = []
    # yList = []
    # for i in range(dataNumber):
    #     x = random.random() * xScale
    #     xList.append(x)
    #     yList.append(np.sin(x) + (random.random()-1.0)*yScale)
    offset1_x = 1.0
    offset1_y = 1.0
    offset2_x = 1.4
    offset2_y = 1.4
    sigma1_x = 0.1
    sigma1_y = 0.15
    sigma2_x = 0.2
    sigma2_y = 0.1
    x1 = np.random.normal(offset1_x, sigma1_x, dataNumber)
    y1 = np.random.normal(offset1_y, sigma1_y, dataNumber)
    x2 = np.random.normal(offset2_x, sigma2_x, dataNumber)
    y2 = np.random.normal(offset2_y, sigma2_y, dataNumber)

    # plt.plot(xList, yList, '.', label='data' )
    plt.plot(x1, y1, '.', label='G1')
    plt.plot(x2, y2, '.', label='G2')
    plt.show()
    for x, y in zip(x1, y1):
        dataList[0].append([x, y])
        dataList[1].append(-1)
    for x, y in zip(x2, y2):
        dataList[0].append([x, y])
        dataList[1].append(1)
    dataList_type2 = []
    for x, y in zip(x1, y1):
        dataList_type2.append([[x, y], -1])
    for x, y in zip(x2, y2):
        dataList_type2.append([[x, y], 1])
    dataList1 = [x1, y1]
    dataList2 = [x2, y2]
    return dataList, dataList1, dataList2, dataList_type2

def alpha_initial(dataNumber=300):
    alpha = []
    for i in range(dataNumber//2):
        alpha.append(1)
    for i in range(dataNumber//2):
        alpha.append(1)
    return alpha

def SUM_part(dataList, alpha, k):
    s = 0.0
    for i in range(len(dataList)):
        yk = dataList[1][k]
        yi = dataList[1][i]
        xk_T = dataList[0][k]
        xi = dataList[0][i]
        xk_T_Multi_xi = 0.0
        for a, b in zip(xk_T, xi):
            xk_T_Multi_xi += (a*b)
        s += alpha[i]*yi*yk*xk_T_Multi_xi

    return s

def svm():
    dataList,_,_,dataList_type2 = generate_dataList()
    dataArray = np.asarray(dataList)
    print(dataList[0])
    print(dataList_type2[0])
    # w = SUM alpha * y_i * x_i
    alpha = alpha_initial()
    iteraterNum = 10
    for i in range(iteraterNum):
        partial_alpha = [-(1-SUM_part(dataList, alpha, k)) for k in range(len(dataList[0]))]
        alpha_Multi_y = 0.0
        for a, b in zip(alpha, dataList[1]):
            alpha_Multi_y += (a*b)
        if alpha_Multi_y > 0:
            New_alpha = []
            for a in alpha[0:len(dataList[0])]:
                New_alpha.append(a+alpha_Multi_y/len(dataList[0]))
            for a in alpha[len(dataList[0]):]:
                New_alpha.append(a)
        else:
            New_alpha = []
            for a in alpha[0:len(dataList[0])]:
                New_alpha.append(a)
            for a in alpha[len(dataList[0]):]:
                New_alpha.append(a+alpha_Multi_y/len(dataList[0]))
        temp = []
        for a, b in zip(New_alpha, partial_alpha):
            temp.append(a+b)
        alpha = temp
        print(alpha)
    return partial_alpha


# m denotes the number of examples here, not the number of features
def gradientDescent(loss, y, theta, alpha, m, numIterations):
    # xTrans = x.transpose()
    for i in range(0, numIterations):
        # hypothesis = np.dot(x, theta)
        # loss = hypothesis - y
        # # avg cost per example (the 2 in 2*m doesn't really matter here.
        # # But to be consistent with the gradient, I include it)
        # cost = np.sum(loss ** 2) / (2 * m)
        # print("Iteration %d | Cost: %f" % (i, cost))
        # # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta

def main():
    svm()

if __name__ == '__main__':
    main()


