
def hello_func():
    print('Hello_func.')
    pass

def hellofun1():
    return 'Hello Function'

print(hello_func)
print(hello_func())

hello_func()
hello_func()
hello_func()
hello_func()

print(hellofun1())
print(hellofun1().upper())

def hello_fun2(greeting, name=',おまえ'):
    return'{} {} Function.'.format(greeting, name)

print(hello_fun2('はじめまして', name='Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art', 'Psychics']
info = {'name': 'John', 'age': 24}

student_info(*courses, **info)

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(days_in_month(2020,2))