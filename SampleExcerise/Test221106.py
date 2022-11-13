from enum import Enum

import pandas as pd


class Color(Enum):
    RED = 'red'
    YELLOW = 'yellow'


i = 10


def function():
    pass


def foo(arg=i):
    print(f"value is ", arg)
    return arg


foo(i)

i = 20
foo(i)
foo()

function()


# Lamda Function
def sayHello(name):
    return lambda value: value + name


name = sayHello('ajay')

print(name('love'))
lovename = sayHello('loveyou')
print(lovename('ajay'))

listInt = [1, 34, 53, 32, 56, 23, 77]
print(listInt)
listInt.sort()
print(listInt)
print(list(('apple', 'banana', 'cherry')))
print(list(range(1, 10)))
print('list(map(lambda x: x*x,listInt)) : ', list(map(lambda x: x * x, listInt)))
print({x: x ** 2 for x in listInt})
for x in list(('apple', 'banana', 'cherry')): print('list value is', x)
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key=lambda v: v[0])
print(pairs)

print('filter', list(filter(lambda x: x % 2 == 0, listInt)))

setValue1 = set({'one', 'two'})
setValue2 = set({'three', 'two'})
print(setValue1)
print(setValue2)
resultantSet = set(setValue1.difference(setValue2))
print(resultantSet)  # one
resultantSet = set(setValue1.intersection(setValue2))
print(resultantSet)  # two
resultantSet = set(setValue2.difference(setValue1))
print(resultantSet)  # three
defaultSet = set()

for x in list(('apple', 'banana', 'cherry')): print('list value', x)
for key, x in enumerate(('apple', 'banana', 'cherry')):
    defaultSet.update({key, x})
print(defaultSet)


def callMap():
    defaultSet = dict()
    for key, x in list('apple', 'banana', 'cherry'):
        defaultSet.update({key: x})
    return defaultSet


print('callMap', callMap)

dataScientist = ({'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'})
dataEngineer = (['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

print('dataScientist of Type Set', type(dataScientist), dataScientist)
print('dataEngineer of Type List', type(dataEngineer), dataEngineer)

# Pandas
rows = [[2, 1, 3], [1, 2, 3], [3, 1, 0], [10, 100, 20],
        [200, 30, 0]]
print(rows[0])
rows_df = pd.DataFrame(rows)
rows_df.columns = ['x', 'y', 'z']

#     x    y   z
# 0    2    1   3
# 1    1    2   3
# 2    3    1   0
# 3   10  100  20
# 4  200   30   0
print(rows_df)
#
# x    2
# y    1
# z    3
print(rows_df.loc[0])
#
#      x   y  z
# 2    3   1  0
# 4  200  30  0
print(rows_df.query('z == 0'))
#
#    0  1  2    3    4
# x  2  1  3   10  200
# y  1  2  1  100   30
# z  3  3  0   20    0
print(rows_df.T)

try:
    # f = open('./main.py')
    # print(f.readline())
    for line in open('./main.py'):
        print(line)
except OSError as fileError:
    print('Error while reading file', fileError)
except Exception as err:
    print('ERROR ', err)


class Point:
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2


point1 = Point(11, 22)
point2 = Point(44, 55)
print(point1.x)
print(point1.y)
print(Point(point2, point1).x)


def returnMulValue():
    return 2, 3, 4, 5


def returnNone():
    print(5)


returnNone()

print(returnMulValue())


def closureMultiplier(value):
    return lambda x: x * value


print(closureMultiplier(6)(5))
print(closureMultiplier(2)(5))
print(closureMultiplier(6)(5))
