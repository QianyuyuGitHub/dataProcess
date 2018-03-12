# -*- coding: <utf-8> -*-
import re

def content1():
    with open("Contents.txt", 'r') as contents:
        with open("NewContents.txt", 'w+') as newContents:
            newContents.write('|Chapter Num & Title|Chapter.Section Num|Section Title|Page out of all|Process State| \n')
            newContents.write('|-|-|-|-|-| \n')
            chapterName = ''
            for line in contents:
                # print(line)
                lineParts = re.search(r'(\d*)(\.*)(\d*)(.*?(?=\d))(\d*)', line)
                # print(lineParts.group(1))
                # print(lineParts.group(2))
                # print(lineParts.group(3))
                # print(lineParts.group(4))
                # print(lineParts.group(5))
                if lineParts.group(2) == '': # this means this line don't have dot, so it's the chapter title
                    # print('No Dot')
                    chapterName = lineParts.group(4)[:-1]# update the current chapter name
                    chapterNum = lineParts.group(1)
                    page = lineParts.group(5)
                    newline = "|" + "**" + chapterNum + " " + chapterName + "**" + "|"*3 + page + "|"*2 + "\n"
                else:
                    chapterNum = lineParts.group(1)
                    page = lineParts.group(5)
                    title_section_num = lineParts.group(1) + '.' + lineParts.group(3)
                    section_name = lineParts.group(4)[:-1]
                    newline = "|"*2 + title_section_num + "|" + section_name + "|" + page + "|"*2 + "\n"

                # newline = "|" + ""
                newContents.write(newline)



def content2():
    with open("Contents2.txt", 'r') as contents:
        with open("NewContents1.txt", 'w+') as newContents:
            newContents.write('|Chapter Num & Title|Chapter.Section Num|Section Title|Page out of all|Process State| \n')
            newContents.write('|-|-|-|-|-| \n')
            count = 0
            ChapterName = ''
            ChapterNum = ''
            for line in contents:
                count += 1
                # lineParts = re.search(r'(\d?)(\.?)(\d?)(\.?)(\d?)(.*(?=\.))(\d*)', line)
                # lineParts = re.search(r'(\d*)(\.*)(\d*)(\.*)(\d*)(\w*|\s*|:*|,*)(\.*)(\d*)', line)
                lineParts = re.search(r'(\d{0,2})(\.?)(\d?)(\.?)(\d?)(.*)(\d{0,3})', line)
                # lineParts = re.search(r'(.*())', line)

                ##test##
                # print(lineParts.group(1), end='*')
                # print(lineParts.group(2), end='*')
                # print(lineParts.group(3), end='*')
                # print(lineParts.group(4), end='*')
                # print(lineParts.group(5), end='*')
                # print(lineParts.group(6), end='*')
                # print(lineParts.group(7))
                ##test##

                lineParts2 = re.search(r'(\s?)(.*(?=\s))(\s)(\d*)', lineParts.group(6))

                ##test##
                # print(lineParts2.group(1), end='*')
                # print(lineParts2.group(2), end='*')
                # print(lineParts2.group(3), end='*')
                # print(lineParts2.group(4))
                ##test##

                if lineParts.group(1) == '':
                    ChapterParts = re.search(r'(.*(?=_))(_)(.*(?=_))(_)(\d*)', lineParts.group(6))
                    ChapterNum = ChapterParts.group(1)
                    ChapterName = ChapterParts.group(3)
                    page = ChapterParts.group(5)
                    print(ChapterNum, end='*')
                    print(ChapterName, end='*')
                    print(page)
                    newline = '|' + '**' + ChapterNum + " " + ChapterName + '**' + '|'*3 + page + '|'*2 + '\n'
                    newContents.write(newline)
                else:
                    sectionNum = lineParts.group(1)+lineParts.group(2)+lineParts.group(3)+lineParts.group(4)+lineParts.group(5)
                    sectionName = lineParts2.group(2)
                    page = lineParts2.group(4)
                    print(sectionNum, end='*')
                    print(sectionName, end='*')
                    print(page)
                    newline = '|'*2 + sectionNum + '|' + sectionName + '|' + page + '|'*2 + '\n'
                    newContents.write(newline)
                    # print(ChapterParts.group(2))

                # if count == 3:
                #     for a in line:
                #         print(ord(a))

if __name__ == '__main__':
    content2()