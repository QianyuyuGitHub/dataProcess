#-*- coding:utf-8 -*-


import csv
import os

path = './IIP3-0.7G-1new/'

def main():
    csvdict = {}
    for dirpath, dirnames, filenames in os.walk(path):
        file_count = 0
        for csvFileSingle in filenames:
            file_count += 1
            # print(csvFile)
            csv_name_path = path + str(csvFileSingle)
            with open(csv_name_path) as csvFile:
                csvReader = csv.reader(csvFile)
                count = 0
                for row in csvReader:
                    count += 1
                    if count == 46:
                        # print(row)
                        csvdict[str(csvFileSingle)] = [row[1]]
                    elif count == 379:
                        csvdict[str(csvFileSingle)].append(row[1])
                    elif count == 713:
                        csvdict[str(csvFileSingle)].append(row[1])
                    elif count == 1046:
                        csvdict[str(csvFileSingle)].append(row[1])
    print(csvdict)
    ave1 = 0.0
    ave2 = 0.0
    ave3 = 0.0
    ave4 = 0.0
    with open('output.csv', 'w+', newline='') as csvFile_out:
        csvWriter = csv.writer(csvFile_out)
        for k in range(210):
            if k < 9:
                temp = k + 1
                fileNum = '00' + str(temp)
            elif k < 99:
                temp = k + 1
                fileNum = '0' + str(temp)
            else:
                temp = k + 1
                fileNum = str(temp)
            name_a = 'Trace_0'
            name_b = '.csv'
            full_name = name_a + fileNum + name_b
            # print(full_name)
            ave1 += float(csvdict[full_name][0])
            ave2 += float(csvdict[full_name][1])
            ave3 += float(csvdict[full_name][2])
            ave4 += float(csvdict[full_name][3])
            if (temp % 10) == 0:
                # csvWriter.writerow([csvdict[full_name][0], csvdict[full_name][1], csvdict[full_name][2], csvdict[full_name][3]])
                csvWriter.writerow(csvdict[full_name])
                csvWriter.writerow([ave1, ave2, ave3, ave4, 'average'])
                ave1 = 0
                ave2 = 0
                ave3 = 0
                ave4 = 0
            else:
                # csvWriter.writerow(
                    # [csvdict[full_name][0], csvdict[full_name][1], csvdict[full_name][2], csvdict[full_name][3]])
                csvWriter.writerow(csvdict[full_name])

def main2(path_list):
    folder_count = 0
    for path in path_list:
        folder_count += 1
        csvdict = {}
        for dirpath, dirnames, filenames in os.walk(path):
            file_count = 0
            for csvFileSingle in filenames:
                file_count += 1
                # print(csvFile)
                csv_name_path = path + str(csvFileSingle)
                with open(csv_name_path) as csvFile:
                    csvReader = csv.reader(csvFile)
                    count = 0
                    for row in csvReader:
                        count += 1
                        if count == 46:
                            # print(row)
                            csvdict[str(csvFileSingle)] = [row[1]]
                        elif count == 379:
                            csvdict[str(csvFileSingle)].append(row[1])
                        elif count == 713:
                            csvdict[str(csvFileSingle)].append(row[1])
                        elif count == 1046:
                            csvdict[str(csvFileSingle)].append(row[1])
        print(csvdict)
        ave1 = 0.0
        ave2 = 0.0
        ave3 = 0.0
        ave4 = 0.0
        csvOutputName = str(folder_count) + '_Output.csv'
        with open(csvOutputName, 'w+', newline='') as csvFile_out:
            csvWriter = csv.writer(csvFile_out)
            for k in range(200):
                if k < 9:
                    temp = k + 1
                    fileNum = '00' + str(temp)
                elif k < 99:
                    temp = k + 1
                    fileNum = '0' + str(temp)
                else:
                    temp = k + 1
                    fileNum = str(temp)
                name_a = 'Trace_0'
                name_b = '.csv'
                full_name = name_a + fileNum + name_b
                # print(full_name)
                ave1 += float(csvdict[full_name][0])
                ave2 += float(csvdict[full_name][1])
                ave3 += float(csvdict[full_name][2])
                ave4 += float(csvdict[full_name][3])
                if (temp % 10) == 0:
                    # csvWriter.writerow(csvdict[full_name])
                    csvWriter.writerow([ave1/10, ave2/10, ave3/10, ave4/10])
                    ave1 = 0
                    ave2 = 0
                    ave3 = 0
                    ave4 = 0
                else:
                    # csvWriter.writerow(csvdict[full_name])
                    pass
if __name__ == '__main__':
    # main()
    path_list = ['./IIP3-0.7G-1new/', './IIP3-0.8G-0new/', './IIP3-0.8G-1new/']
    main2(path_list)