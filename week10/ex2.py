#강아지 객체를 만들기 위한 Dog 클래스 작성
#속성(field) - 이름(name), 개월수(age), 색상(color)
class Dog:
    name = ''
    age = 0
    color = ''

#main code
#객체 인스턴스 생성
mydog = Dog()
mydog.name = '쿠키'
mydog.age = 8
mydog.color = 'brown'

print(f'우리집 강아지는 {mydog.age}개월 된 {mydog.name}입니다.')
print(f'색상은 {mydog.color}입니다.')