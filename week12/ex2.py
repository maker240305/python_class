#파일의 내용을 통째로 읽어서 처리
inFile = open('c:/Temp/python2/data1.txt', 'r', encoding='utf-8')

inList = inFile.readlines()
#print(inList)
for inStr in inList:
    print(inStr, end='')

inFile.close()