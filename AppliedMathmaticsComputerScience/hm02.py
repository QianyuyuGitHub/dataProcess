# -*- coding:utf-8 -*-

'''
This file is created by Yuyu Qian, Computer Science and Technology Department, Zhejiang University
qianyuyulys@gmail.com
This code could be used for any non-commercial purpose. You can edit and reconstruct it. When you use this code please
cite the author.
'''

import numpy as np
import matplotlib.pyplot as mplt
from PIL import Image
import re
# with open('optdigits-orig.tra', 'rb') as data:
#     count = 0
#     dataList = [[]]
#     labelList = []
#     pixels = 32 * 32
#     for line in data:
#         for bit in line:
#             if bit != '\n' and bit != ' ':
#                 if count != pixels:  # if hasn't count to pixels max:
#                         dataList[-1].append(bit)
#                         count += 1
#                 elif count == pixels: # this is the class label
#                         labelList.append(bit)
#                         dataList.append([])
#                         count = 0
#     # print(np.shape(dataList))
#     print(dataList[0][:32*32])
#     # print(labelList)


#	'\n' at the end of each row to visualize input.
#	The last attribute is the class code 0..9


# the digit tra file contain 21 lines of instructions
# with open('optdigits-orig.tra', 'rb') as data:
#     count = 1
#     for line in data:
#         if count == 22:
#             print(line)
#         count+=1

def dataGet(CertainType = b' 3'):
    with open('optdigits-orig.tra', 'rb') as data:
        lineCount = -21
        dataList = [[]]
        labelList = []
        for line in data:
            if lineCount != 32 and lineCount >= 0:
                newLine = line.rstrip(b'\n')
                dataList[-1].append(newLine)
                lineCount += 1
            elif lineCount == 32:  # this is the last line of a a digit matrix, which denotes the label
                newLine = re.sub(b' +', b' ', line)
                newLine = newLine.rstrip(b'\n')
                labelList.extend([newLine])
                dataList.append([])
                lineCount = 0
            else:
                lineCount += 1
        dataList = dataList[:-1]


        # print(dataList)
        # print(np.shape(dataList))
        # print(np.shape(labelList))


        # #####this for showing the result of bit matrix
        # count = 0
        # for digit in dataList:
        #     if count == 0:
        #         print(digit)
        #         ccount = 0
        #         for bits in digit:
        #             print(bits)
        #             if ccount == 0:
        #                 for bit in bits:
        #                     print(bit)
        #                 ccount += 1
        #     count += 1
        # #################

    # print(dataList)
    newDatalist = []
    for digit in dataList:
        newDigit = []
        for bits in digit:  # one line of digit
            newBits = []
            for bit in bits:
                if bit == 48:
                    newBits.append(0)
                elif bit == 49:
                    newBits.append(1)
                else:
                    print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!")
            newDigit.append(newBits)
        newDatalist.append(newDigit)

    # newLabelList = []
    # for label in labelList:


    # print(np.shape(newDatalist))
    # print(newDatalist[0])


    xMat_reashape = []
    for digit in newDatalist:
        xList = []
        for line in digit:
            xList.extend(line)
        xMat_reashape.append(xList)
    # print(xMat_reashape)

    xMat_certain_type = []
    for label, digit in zip(labelList, xMat_reashape):
        if label == CertainType:
            xMat_certain_type.append(digit)
    # print("xMat_certain_type", xMat_certain_type)
    # print(np.shape(xMat_certain_type))

    xMat_reashape = np.asmatrix(xMat_reashape)
    yMat = np.asmatrix(labelList)
    xMat_certain_type = np.asmatrix(xMat_certain_type)
    return xMat_reashape, yMat, xMat_certain_type, newDatalist


def pac(xMat):
    num_data, dim = xMat.shape
    mean_xMat = xMat.mean(axis=0)
    # xMat = xMat - mean_xMat
    if dim > num_data:
        M = np.dot(xMat, xMat.T)
        # Return the eigenvalues and eigenvectors of a Hermitian or symmetric matrix.
        e, EV = np.linalg.eigh(M)
        tmp = np.dot(xMat.T, EV).T
        V = tmp[::-1]  # reverse orders
        S = np.sqrt(e)
        S = S[::-1]
        for i in range(V.shape[1]):
            V[:, i] /= 5
    else:
        U, S, V = np.linalg.svd(xMat) #Singular Value Decomposition.
        V = V[:num_data]

    return V, S, mean_xMat

def pac_singular(xMat):
    # print(xMat)
    num_data, dim = xMat.shape
    sp = xMat.shape
    regular_offset = 0.5 * np.ones(sp)
    # print(regular_offset)


    range_x, range_y = xMat.shape
    xMat_float = []
    for i in range(range_x):
        xMat_float.append([])
        for j in range(range_y):
            # print(xMat.item((i, j)))
            if xMat.item((i, j)) == 0:
                xMat_float[-1].append(0.0)
            elif xMat.item((i, j)) == 1:
                xMat_float[-1].append(1.0)
    # print(np.shape(xMat_float))
    # print(xMat_float)

    # xMat_float -= regular_offset
    # mean_xMat = xMat_float.mean(axis=0)
    # xMat_float = xMat_float - mean_xMat
    # U, S, V = np.linalg.svd(xMat_float) #Singular Value Decomposition.
    mean_xMat = xMat.mean(axis=0)
    xMat = xMat - mean_xMat
    U, S, V = np.linalg.svd(xMat) #Singular Value Decomposition.
    V = V[:num_data]

    return V, S, mean_xMat, U

def main():
    pixel_x = 32
    pixel_y = 32
    xMat, yMat, xMat_certain_type, xMat_mat = dataGet()
    # pac(xMat, yMat)
    # print(np.shape(xMat_certain_type))  # there are 199 '3' in the dataset
    V, S, mean_xMat, U = pac_singular(xMat_certain_type)
    mplt.figure(1)

    mplt.gray()
    mplt.subplot(2, 4, 1)
    # mplt.imshow(mean_xMat.reshape(pixel_x, pixel_y))
    for i in range(8):
        mplt.subplot(2, 4, i+1)
        mplt.imshow(V[i].reshape(pixel_x, pixel_y))

    print(S.shape)
    print(V.shape)
    print(S)
    # for mat in xMat_mat:
    #     print(np.dot(mat, ))
    print(U)
    mplt.matshow(V) # show the matrix U
    # print(U.shape)
    # result = np.dot(xMat_certain_type.T, U)
    # print(result)


    # projective
    axis_1 = []
    axis_2 = []
    for image in xMat_certain_type:
        matResult_1 = np.dot(image, V[0].T)
        matResult_2 = np.dot(image, V[1].T)
        axis_1.append(matResult_1.item((0,0)) )# image(1024, ) v[i](1024, )
        axis_2.append(matResult_2.item((0,0)) )# image(1024, ) v[i](1024, )
    print(axis_1)
    print(axis_2)
    # projective

    target1 = [-4.0, -2.0, 0.0, 2.0, 4.0]
    target2 = target1[::-1]
    print(target2)
    target_coord_list = []
    for y in target2:
        for x in target1:
            target_coord_list.append([x, y])

    plot_target_real_coord = []
    for target_coord in target_coord_list:
        distance = 10.0**6
        plot_target_real_coord.append([])
        for x, y in zip(axis_1, axis_2):
            if ((x-target_coord[0])**2 + (y-target_coord[1])**2) < distance:
                distance = ((x-target_coord[0])**2 + (y-target_coord[1])**2)
                plot_target_real_coord[-1] = [x, y]
    print(plot_target_real_coord)
    point_out_x = []
    point_out_y = []
    for x, y in plot_target_real_coord:
        point_out_x.append(x)
        point_out_y.append(y)

    # # have to use this method to duplicate the list, otherwise , it's just a link
    # import copy
    # axis_1_sort = copy.copy(axis_1)
    # axis_2_sort = copy.copy(axis_2)
    # # axis_1_sort = axis_1
    # # axis_2_sort = axis_2
    # axis_1_sort.sort()
    # axis_2_sort.sort()
    # point_out_x = []
    # point_out_y = []
    # for i in np.arange(0, len(axis_1_sort), len(axis_1_sort)//5):
    #     point_out_x.append(axis_1_sort[i])
    #     point_out_y.append(axis_2[axis_1.index(axis_1_sort[i])])
    # mplt.plot(point_out_x, point_out_y, 'ro')

    mplt.figure(3)
    mplt.plot(axis_1, axis_2, 'go')
    mplt.plot(point_out_x, point_out_y, 'ro')
    # mplt.scatter(x, y, marker='^')

    mplt.figure(4)
    mplt.gray()
    mplt.subplot(5, 5, 1)
    i = 0
    for x, y in plot_target_real_coord:
        mplt.subplot(5, 5, i+1)
        mplt.imshow(xMat_certain_type[axis_1.index(x)].reshape(pixel_x, pixel_y))
        i += 1

    mplt.show()


if __name__ == '__main__':
    main()
