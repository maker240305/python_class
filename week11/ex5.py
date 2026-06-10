#메서드 재정의 실습 예제
#부모 클래스 선언
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def getSalary(self):
        salary = super().getSalary() + self.bonus
        return salary

    def info(self):
        print(f'이름:{self.name}, 월급:{self.salary}, 보너스:{self.bonus}')

kim = Manager('김철수',250,100)
kim.info()
print(f'최종 급여 = {kim.getSalary()}')

