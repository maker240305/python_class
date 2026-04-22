#문자열 실습
#이메일 정보에서 아이디 추출하기
email = 'python1234@naver.com'
id = email.split('@')
print(id[0])
print(email.split('@')[0])  #한문장으로 표현하기

#비밀번호 일부 마스킹하기
# python1234 => ********34 로 출력하기
password = input('비밀번호 입력 : ')
length = len(password)
mask1 = '*' * (length-2)
mask2 = password[-2:]
result = mask1 + mask2
print(result)