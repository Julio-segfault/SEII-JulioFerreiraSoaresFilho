
from operator import attrgetter

li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)

li.sort(reverse=True)

print('Sorted Variable:\t', li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)

li1 = [-9,-1,-8,-2,7,3,6,4,5]
s_li1 = sorted(li1, key=abs)
s_li1

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '{},{},${}'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

def e_sort2(emp):
    return emp.age

def e_sort3(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort)
s_employees2 = sorted(employees, key=e_sort2)
s_employees3 = sorted(employees, key=e_sort3, reverse=True)

s_employees4 = sorted(employees, key=lambda e: e.name)

s_employees5 = sorted(employees, key=attrgetter('age'))

print(s_employees)
print(s_employees2)
print(s_employees3)
print(s_employees4)
print(s_employees5)