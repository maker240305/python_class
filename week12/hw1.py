outFile = open('C:/Users/john0/OneDrive/바탕 화면/202644072_윤인식.txt','w')

qslist = ['이름 : ','좋아하는 노래 : ','가장 인상깊게 본 영화 : ','최근에 다녀온 여행지 : ','제일 좋아하는 음식 : ','추천 맛집 소개 : ']

for i in qslist:
    outStr = input(i)
    outFile.writelines(i + outStr + '\n')

outFile.close()
print('---파일 쓰기 완료---')