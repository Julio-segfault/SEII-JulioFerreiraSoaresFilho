

import builtins
x = 'global x'
z = 'global z'

m = min([5, 1, 3, 2, 4])
print(m)

def test(z):
    #global x
    y = 'local y'
    x = 'local x'
    z = 'local z'
    print(z)
    print(y)
    print(x)

def my_min():
    pass

def outer():
    x = 'outer x'
    def inner():
        #nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)


test(z)
print(x)
print(z)

outer()
print(x)
#print(dir(builtins))