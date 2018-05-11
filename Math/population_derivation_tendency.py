import numpy as np

a_out = 0.3
a_in = 1-a_out
b_out = 0.7
b_in = 1-b_out


def cal_mat_multipy():
    mat_a = np.array([[a_out, b_out], [a_in, b_in]])
    mat_result = np.array([[a_out, b_out], [a_in, b_in]])
    Last_result = np.array([[1.0, 1.0], [1.0, 1.0]])
    while (not np.array_equal(Last_result, mat_result)):
        Last_result = np.copy(mat_result)
        mat_result = np.copy(np.matmul(mat_result, mat_a))

    print(mat_result)
    return mat_result

def main():
    mat_result = cal_mat_multipy()

if __name__ == '__main__':
    main()