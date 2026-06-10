#파일을 이용한 출력
#키보드를 입력한 내용을 파일에 쓰기
outFile = open('c:/Temp/python2/data2.txt','w')

#빈 문자열이 입력되기 전까지 파일에 쓰기
#빈 문자열이 들어오면 종료
while True:
    outStr = input('내용 입력 : ')
    if outStr == '':
        break
    outFile.writelines(outStr+'\n')

outFile.close()
print('---파일 쓰기 완료---')