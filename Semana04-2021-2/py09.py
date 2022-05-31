
#import module09
#import module09 as mm
import sys
#sys.path.append('/home/')

import random
import math
import datetime
import calendar
import os

from module09 import find_index, test
#from module09 import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)
print(sys.path)

print(random.choice(courses))
print(math.radians(90), math.sin(math.radians(90)), sep='  -  ')

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)