class Person():
    def __init__(self, workTime=0, paymentPerHour=0, workDay=0, salary=0):
        self.workTime = workTime
        self.paymentPerHour = paymentPerHour
        self.workDay = workDay
        self.salary = salary

    def payment(self):
        self.salary = self.workTime * self.paymentPerHour * self.workDay
        return


class Boss(Person):
    def __init__(self, workerCount=0, totalSalary=0):
        super().__init__()
        self.totalSalary = totalSalary
        self.workerCount = workerCount
        self.salary = 0
        self.workTime = 7
        self.paymentPerHour = 1000
        self.workDay = 22

    def payment(self):
        self.salary = (self.workTime * self.paymentPerHour * self.workDay) - self.totalSalary


class Worker(Person):
    def __init__(self, sale=0):
        super().__init__()
        self.sale = sale
        self.salary = 0
        self.workTime = 7
        self.paymentPerHour = 25
        self.workDay = 26

    def payment(self):
        self.salary = (self.workTime * self.paymentPerHour * self.workDay) + (self.sale * (self.paymentPerHour * 2 / 5))
        return


Ege = Boss()

Koray = Worker(sale=10)

AyberkKole = Worker(sale=4)

Ugur = Worker(sale=2)

workers = [Koray, AyberkKole, Ugur]

Ege.workerCount = workers.__len__()

totalSalary = 0

Ege.payment()

print('Maas:', Ege.salary)

for item in workers:
    item.payment()
    totalSalary = totalSalary + item.salary
    print('Maas:', item.salary)

Ege.totalSalary = totalSalary

print("Tum maaslar: ", totalSalary)

Ege.payment()

print('Maas:', Ege.salary)