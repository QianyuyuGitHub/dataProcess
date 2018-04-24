#-*- coding:utf-8 -*-
'''
A teaching demo

Created by Yuyu Qian
Created by Yuyu Qian
'''
import csv
import os

filePath = './IIP3-0.7G-1new/Trace_0001.csv' # this is the path of the .csv file you want to operate with

with open(filePath, 'r') as csvFile: # use "with" syntax can certain it will close the file after processes
    for row in csvFile:
        print(row, end='')
for x in range(2):
    print(x)
