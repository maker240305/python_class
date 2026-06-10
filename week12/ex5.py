#파일 안의 점수를 읽어서 총점과 평균을 다른 파일에 쓰기

inFile = open('c:/Temp/python2/sample.txt','r',encoding='utf-8')
outFile = open('c:/Temp/python2/result.txt','w')

scoreList = inFile.readlines()
total = 0
for score in scoreList:
    total += int(score)

ave = total/len(scoreList)

outFile.writelines(f'total = {total}점\nave = {ave}점')

inFile.close()
outFile.close()
print('-- 성적 처리 완료 --')
