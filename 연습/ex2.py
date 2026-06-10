class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

    def printInfo(self):
        print(f'이름: {self.name} / 급여: {self.salary}만원')

class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def getSalary(self):
        return self.salary + self.bonus

emp1 = Employee('이영희',200)
manager1 = Manager('김철수',250,100)

emp1.printInfo()
manager1.printInfo()

print(f'{emp1.name} 최종 급여: {emp1.getSalary()}만원')
print(f'{manager1.name} 최종 급여: {manager1.getSalary()}만원')