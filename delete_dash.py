import os
import re

dash_count = 0
new_line = []
with open("D.txt", 'r') as textFile:
    for line in textFile:
        # print(line)
        regular = re.search(r'^(-)(.*)', line)
        if regular:
            print(regular.group(2))
            dash_count += 1
            new_line.append( regular.group(2) )
        else:
            new_line.append( line )
with open("New.txt", 'w+') as writeFile:
    for line in new_line:
        writeFile.write(line + '\n')