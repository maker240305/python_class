#파일 입출력
#파일의 내용을 읽어서 화면 출력하기
#1.파일 열기
inFile = open('c:/Temp/python2/data1.txt','r',encoding='utf-8')

#2.파일 읽기 - 한 줄씩 읽기
#반복문 적용하기
while True:
    inStr = inFile.readline()
    if inStr == '':
        break
    print(inStr, end='')

#3.파일 닫기
inFile.close()