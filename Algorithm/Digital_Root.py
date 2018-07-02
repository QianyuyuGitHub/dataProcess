def digital_root(n):
    # ...
    r = n
    while (r > 9):
        temp = r
        r = 0
        while (temp > 0):
            print(temp)
            r += (temp % 10)
            temp //= 10
    return r

print(digital_root(16))