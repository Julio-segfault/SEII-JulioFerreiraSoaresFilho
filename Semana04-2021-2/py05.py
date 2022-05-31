
student1 = {'name': 'John', 'age': 25, 'courses': ['Math','Compsci']}
#student1 = {1: 'John', 'age': 25, 'courses': ['Math','Compsci']}
student = student1.copy()

print(student)
print(student['name'])
print(student['courses'])
#print(student['phone'])
print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))
student['name'] = 'Jane'
print(student)

student.update({'name': 'John', 'age': 26, 'phone': '666-6666'})
print(student)

del student['age']
print(student)
std = student1.copy()
age = std.pop('age')
print(age)
print('-----')

std = student1.copy()
print(len(std))
print(std.values())
print(student.items())

print('-----')
for key, value in std.items():
    print(key, value)
