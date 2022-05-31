
if True:
    print('Conditional was true')
if False:
    print('Conditional was false')

language = 'Java'

if language == 'Python':
    print('Python')
elif language == 'Java':
    print('Java')
elif language == 'JavaScript':
    print('JavaScrpt')
else:
    print('Not Python')

user = 'Admin'
logged = False

if user == 'Admin' or logged:
    print('Admin Page')
else:
    print('404 not found')

if not logged:
    print('Log-in')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]
c = a

print(id(a), id(b), id(c), a == b, a is b, a is c, id(a) == id(b), sep='\n')

print('-----')

condition = ['False', 'None', 0, 69, '', [], {}, 'Test', [1, 2, 3]]


for index in condition:
    if index:
        print(index, 'is True')
    else:
        print(index, 'is False')