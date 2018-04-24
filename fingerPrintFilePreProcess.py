# -*- coding=utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def hex_have_two_sub_convert_to_decimal(hex_have_two):
    ISTEST = 1
    hex_with_0x = int(hex_have_two, 16)
    if ISTEST:
        print(format(hex_with_0x, '#010b')[2:])
    return format(hex_with_0x, '#010b')[2:]

def main():
    ISTEST = 0
    file_name = "lysfinger.txt"
    start_bit = "0:UART: RX/TX\n"
    stop_bit = "0:UART: RX/TX\n"
    with open(file_name) as fp_file:
        line_count = 0
        the_whole_file_hex = []
        the_whole_file_binary = []
        for line in fp_file:
            # print(line, end='')
            _, _, c = line.split(',', 2)
            # print(c.rstrip()) # print all the third part of one line
            # print(c)
            if line_count == 1:
                start_bit = "Start bit\n"
                stop_bit = "Stop bit\n"
            if (c != start_bit) and (c != stop_bit):
                # print(c.rstrip())  # only print the data every three lines
                # print(len(c))
                if c[0] != '[' or ((c[0] == '[') and (c[1] == '\n')):
                    if ISTEST:
                        # print(ord(c[0]))  # print the unicode number from char but in decimal
                        # print(format(ord(c[0]), '#04X'))  # get the hex number converted from char
                        print(format(ord(c[0]), '#04X')[2:])  # get the hex number without 0x
                    hex_without_0x = format(ord(c[0]), '#04X')[2:]
                    the_whole_file_hex.append(hex_without_0x)
                    # print(hex_without_0x[0])
                    # print(hex_without_0x[1])
                    the_whole_file_binary.append(hex_have_two_sub_convert_to_decimal(format(ord(c[0]), '#04X')))

                elif c[0] == '[' and c[1] != '\n':
                    if ISTEST:
                        print(c[1:-2])
                    the_whole_file_hex.append(c[1:-2])
                    the_whole_file_binary.append(hex_have_two_sub_convert_to_decimal(("0x"+c[1:-2])))

            line_count += 1
            # if line_count == 1260:
            #     print("the final is:", c)
            #     break
        # print(the_whole_file)

        print(the_whole_file_binary)
        print(len(the_whole_file_binary))
        print(line_count)
        # rewrite the whole file again:
        image_one_hot = []
        image_binary_one_hot = []
        with open("finger_new.txt", 'w+') as newfp_file:
            byte_count = -26
            out_count = 0
            for item in the_whole_file_binary:
                if byte_count < 0:  # file head
                    byte_count += 1
                elif byte_count < 14:  # communication script
                    byte_count += 1
                elif byte_count < 509:
                    newfp_file.write(item)
                    image_one_hot += item
                    if item[5] == '1' or item[6] == '1' or item[7] == '1':
                        binary_bit = 0
                        image_binary_one_hot.append(binary_bit)
                    else:
                        binary_bit = 1
                        image_binary_one_hot.append(binary_bit)
                    out_count += 1
                    byte_count += 1
                else:
                    newfp_file.write(item)
                    image_one_hot += item
                    if item[5] == '1' or item[6] == '1' or item[7] == '1':
                        binary_bit = 0
                        image_binary_one_hot.append(binary_bit)
                    else:
                        binary_bit = 1
                        image_binary_one_hot.append(binary_bit)
                    out_count += 1
                    byte_count = 0
        print(out_count)
        binary_string = ''.join(image_one_hot)
        byte_matrix = np.reshape(image_one_hot, (8*242, 266))
        print(byte_matrix)
        binary_matrix = np.reshape(image_binary_one_hot, (242, 266))
        print(binary_matrix)
        binary_array = np.asarray(binary_matrix)
        # plt.figure(1)
        # plt.gray()
        plt.imshow(binary_array, cmap='Greys')
        plt.show()

if __name__ == '__main__':
    main()
    # result = hex_have_two_sub_convert_to_decimal("0xFA")
    # print("aaa,bbb,,".split(',', 2))