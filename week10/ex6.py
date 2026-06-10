#매개변수가 있는 생성자 실습
#Student
#field - name, major
#생성자 매개변수 - name, major
class Student:
    name = ''
    major = ''

    def __init__(self,name,major):
        self.name = name
        self.major = major

    def printInfo(self):
        print(f'{self.name} 학생은 {self.major} 소속입니다.')

hong = Student('홍길동','소프트웨어공학과')
lee = Student('이순신','컴퓨터공학과')
hong.printInfo()
lee.printInfo()