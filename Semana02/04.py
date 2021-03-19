
courses = ['History','Meth', 'Phisics', 'Compsci']

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])

#print(courses[4])

print(courses[0:2])
print(courses[:2])
print(courses[2:])

#courses1 = courses, this attributes the actual list, try method copy
courses1 = courses.copy()
courses1.append('Art')
print(courses1)

#resetting a list without copy
courses1.clear()
courses1.extend(courses)


print('---1---')
print(courses1)
courses1.insert(0,'Art')
print(courses1)
print('---2---')


courses1 = courses.copy()
#print('---', courses1)
courses_2 = ['Art', 'Education']
courses1.insert(0,courses_2)
print(courses1)

print('---3---')
courses1 = courses.copy()
courses1.extend(courses_2)
print(courses1)

print('---4---')
courses1 = courses.copy()
courses1.remove('Meth')
print(courses1)
courses1 = courses.copy()
popped = courses1.pop()
print(popped)
print(courses1)

print('---5---')
courses1 = courses.copy()
courses2 = courses.copy()
courses1.reverse()
courses2.sort()
print(courses1 , courses2, sep='\n')

print('---6---')
courses1 = courses.copy()
num = [1, 5, 2, 4, 3]
courses1.sort()
num.sort()
print(courses1)
print(num)
courses1.sort(reverse=True)
num.sort(reverse=True)
print(courses1)
print(num)
courses2 = sorted(courses)
print(courses2)
print(min(num))
print(max(num))
print(sum(num))

print('---7---')
courses1 = courses.copy()
print(courses1.index('Compsci'))
#print(courses1.index('CompSci'))
print('Meth' in  courses1)
print('Pollos' in courses1)

print('---7---')
for item in courses1:
    print(item)
for course in courses1:
        print(course, end=' ')
for index, k in enumerate(courses1, start=1):
        print(index, k)

print('---8---')
courses1 = courses.copy()
course_str = ' - '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)


# Mutable
print('---9---')
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


#Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}

print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# # Empty Lists
# empty_list = []
# empty_list = list()
#
# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()
#
# # Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()