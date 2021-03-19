
num = [1, 2, 3, 4, 5]

for i in num:
    print(i, end='-')

print(end='\n')
for k in num:
    if k ==2:
        print('...')
        continue
    if k == 4:
        print('見つけた')
        break
    print(k)

print('გმადლობთ')

for k in num:
    for letter in 'abc':
        print(k,letter)

print('-----')

for i in range(3,11):
    print(i)

print('გმადლობთ')
print('-----')

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x+=1