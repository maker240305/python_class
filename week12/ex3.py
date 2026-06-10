#파일을 자동으로 close하는 방법: with ~ as
with open('c:/Temp/python2/data1.txt', 'r',encoding='utf-8') as inFile:
    inList = inFile.readlines()
    for inStr in inList:
        print(inStr, end='')

