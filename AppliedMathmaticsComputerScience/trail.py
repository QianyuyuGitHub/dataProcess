import numpy as np

row = 4
col = 4

m = [[1,2,0,4],[1,0,0,4],[8,1,0,1],[9,0,0,1]]

def greater0_minus_row(digit):
    if digit < 0:
        return 0
    elif digit >= row:
        return row - 1
    else:
        return digit


def greater0_minus_col(digit):
    if digit < 0:
        return 0
    elif digit >= col:
        return col - 1
    else:
        return digit


def even(imageOneChannel):
    for r in range(row):
        for c in range(col):
            sum = 0
            for i in range(9):
                sum += imageOneChannel[greater0_minus_row(r - 1 + i // 3), greater0_minus_col(c - 1 + i % 3)]
            imageOneChannel[r, c] = sum // 9
    return imageOneChannel

marr = np.asarray(m)
print(marr)
mm = even(marr)

print(mm)