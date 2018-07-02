import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import os
import random as rd

def img_show(img, title="Rotated Image"):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate_expand_with_white(original_img, degree, blur_argument=9):
    rows, cols, _ = original_img.shape
    min_radius = int(np.sqrt((rows/2) ** 2 + (cols/2) ** 2)) + 1
    # white_background = np.ones((2*min_radius, 2*min_radius), np.uint8)
    white_background = np.full((2*min_radius, 2*min_radius, 3), 255, dtype=np.uint8)

    # rows_, cols_ = white_background.shape

    # x-axis offset:
    offset_cols = (min_radius - cols)//2
    # y-axis offset:
    offset_rows = (min_radius - rows)//2

    for row in range(rows):
        for col in range(cols):
            # x
            x = col - cols/2
            # y
            y = rows/2 - row
            col_mapping = int(x * np.cos(degree) - y * np.sin(degree))
            row_mapping = int(x * np.sin(degree) + y * np.cos(degree))
            white_background[int(min_radius) - row_mapping][col_mapping+int(min_radius)] = original_img[row][col]
            # white_background[row][col] = original_img[row][col]

    ############ To Avoid Some Strange Patten
    expanded_img = np.full((2*min_radius, 2*min_radius), 255, dtype=np.uint8)
    for row in range(2*min_radius):
        for col in range(2*min_radius):
            sum = 0
            for row_offset in np.arange(int(-blur_argument/2), int(blur_argument/2) + 1):
                for col_offset in np.arange(int(-blur_argument/2), int(blur_argument/2) + 1):
                    if (row + row_offset) < 2*min_radius and (col + col_offset) < 2*min_radius and (row + row_offset) > 0 and (col + col_offset) > 0:
                        sum += white_background[row + row_offset][col + col_offset]
                    else:
                        sum += white_background[row][col]
            expanded_img[row][col] = sum / (blur_argument*blur_argument)


    label = "Rotated by:" + str(degree / (np.pi / 6) * 30) + " D"
    return white_background, label

def rotate_expand_with_white_mapping_from_bigger_image(original_img, degree):
    rows, cols, _ = original_img.shape
    min_radius = int(np.sqrt((rows/2) ** 2 + (cols/2) ** 2)) + 1
    # white_background = np.ones((2*min_radius, 2*min_radius), np.uint8)
    white_background = np.full((2*min_radius, 2*min_radius, 4), 255, dtype=np.uint8)

    for row in range(2*min_radius):
        for col in range(2*min_radius):
            # x
            x = col - min_radius
            # y
            y = min_radius - row
            col_mapping = int(x * np.cos(degree) - y * np.sin(degree))
            row_mapping = int(x * np.sin(degree) + y * np.cos(degree))

            y_inner = int(rows/2) - row_mapping
            x_inner = col_mapping + int(cols/2)
            if 0<= x_inner <cols and 0<= y_inner <rows:
                white_background[row][col] = original_img[y_inner][x_inner]
            else:
                white_background[row][col] = [255,255,255,0]
            # white_background[row][col] = original_img[row][col]


    label = "Rotated by:" + str(degree / (np.pi / 6) * 30) + " D"
    return white_background, label

def rotate(img, degree):
    rows, cols = img.shape
    rotated_mat = cv.getRotationMatrix2D((cols/2, rows/2), degree, 1)
    rotated_img = cv.warpAffine(img, rotated_mat, (cols, rows))
    return rotated_img

def main():
    # img = cv.imread('husky.jpg', 3)
    # cv.imshow("Apple Mark", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    # print(img.shape)
    #
    # print(int(-5/2))
    # print(int(5/2))
    # print(np.arange(-2,2))
    outputDir = "./rotated/"

    filenameList = []
    for root, dirs, files in os.walk("./imgs/"):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                file_path = os.path.join(root, file)
                print("Find image:", os.path.join(root, file))
                filenameList.append(file_path)

    # print(filenameList)
    count = 0
    for filename in filenameList:
        img = cv.imread(filename, 8) # four channel
        for i in np.arange(0, 360/30):
            degree = i * (np.pi / 6)

            # rotated_img = rotate(img, degree / (np.pi / 6) * 30)
            # img_show(rotated_img)

            # print(rotated_img)
            expanded_img, label = rotate_expand_with_white_mapping_from_bigger_image(img, degree)
            # img_show(expanded_img, label)
            # cv.imwrite("./rotated/"+ str(filename[2:-4]) + '_' + str(int(degree / (np.pi / 6) * 30)) +'.png', expanded_img)
            cv.imwrite(outputDir + str(count) + '_' + str(int(degree / (np.pi / 6) * 30)) +'.png', expanded_img)
            print("Output:", str(filename[:-4]) + '_' + str(int(degree / (np.pi / 6) * 30)) +'.png')
        count += 1
if __name__ == '__main__':
    main()




# rows, cols = img.shape
# M = cv.getRotationMatrix2D((cols/2, rows/2), 30, 1)
# dst = cv.warpAffine(img, M, (cols, rows))
#
# cv.imshow("Rotated Image", dst)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
#
#
# min_radius = int(np.sqrt((rows/2) ** 2 + (cols/2) ** 2)) + 1
# print(min_radius)
# # sm = [[255, 255, 255] for i in range(min_radius ** 2)]
# # sm = [100 for i in range(min_radius ** 2)]
# sm = np.ones((2*min_radius, 2*min_radius), np.float32)
#
#
#
# ar = np.array(sm)
# print("shape of array:", ar.shape)
# # reshaped_ar = ar.reshape(min_radius, min_radius,3)
#
# # reshaped_ar = ar.reshape(min_radius, min_radius)
# # print("shape of new array:", reshaped_ar.shape)
#
# # cv.imwrite('mat_img.jpg', reshaped_ar)
# # cv.imshow("Mat", reshaped_ar)
# cv.imshow("Mat", ar)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
# array_image = np.asarray(img)
# print(array_image.shape)
# print(array_image)
