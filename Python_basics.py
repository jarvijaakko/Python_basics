# Catching up with some Python basics first time in a long time

# Inputting strings
print('Give me your name:')
name = input()
print('Hello', name)

# Operators
print('Pick a number: ')
num1 = input()
print('Pick another number: ')
num2 = input()

sum = int(num1) + int(num2)

print(sum)

print(num1/num2) # Division
print(num1**num2) # Power
print(num1//num2) # Integer division
print(num1%num2) # Modulus

# Conditions (<>)
print(4 != 5)

# If/else
print('How old are you? ')
age = input()

if int(age) >= 18:
    print('You are an adult')
else:
    print('You are a child')

# Chained conditionals (and, or, not)
print('How old are you? ')
age = input()

if int(age) >= 18:
    print('You are an adult')
elif (int(age) >= 15) and (int(age) < 18):
    print('You are a teenager')
else:
    print('You are a child')

# Nested statements
x = 2
y = 3
if x == 2:
    if y == 3:
        print('x = 2 and y = 3')
    else:
        print('x = 2 but y != 3')
else:
    print('x != 2')

# For loops
for x in range(0, 10, 1): # (start, stop, step)
    print(x)

# While loops
loop = True

while loop:
    password = input('Enter password: ')
    if password == 'salasana':
        break

# Lists
fruits = ['apple', 'pear', 3]
print(fruits)
fruits.append('strawberry') # Append adds an item to a list
print(fruits)
fruits[1] = 'blueberry'
print(fruits)

# Tuples
position = (2, 3) # Similar to a list but with normal brackets
color = (255, 255, 255)
print(type(color))

# Iteration by item
fruits = ['apples', 'pears', 'strawberries']
for fruit in fruits:
    print(fruit)

for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')

# String methods
text = input('Input something: ')
print(text.strip()) # Strip removes whitespace around the word

text = input('Input something: ')
print(len(text)) # Length of the text

text = input('Input something: ')
print(text.lower()) # Lowercase

text = input('Input something: ')
print(text.upper()) # Uppercase

text = input('Input something: ')
print(text.split()) # Makes a list of given words based on the delimiter (defaults to space as delimiter)

# Slice operator
fruits = ['apples', 'pears', 'strawberries']
text = 'Hello I like python'
print(text[1:10:2]) 

fruits[5:5] = 'b' # It is possible to add to a certain point in a list with slice
print(fruits)

# Functions
def addTwo(x):
    return x + 2
print(addTwo(7))

def subtractTwo(x):
    return x - 2
print(subtractTwo(7))

def printString(string):
    print(string)
printString('jee')

# Reading from text file
# Option 1: \n in the end of each line
file = open('Jee.txt', 'r')
f = file.readlines()
print(f)

# Option 2: Iterate over list elements
file = open('Jee.txt', 'r')
f = file.readlines()

newList = []
for line in f:
    newList.append(line.strip())
print(newList)
file.close()

# Writing to a text file
file = open('Jee.txt', 'w')
file.write('python\n')
file.write('Jee jee is a very good name for a variable')
file.close()

# .find() and .count() methods
string = 'hello'
print(string.find('o'))

string = 'hello'
print(string.count('l'))

# Modular programming
import math
import myModule
print(math.degrees(math.pi))

print(myModule.myFunc(4))
print(myModule.anotherFunc(10))

# Optional parameters
def func(x, text='2'):
    print(x)
    if text == '1':
        print('Text is one')
    else:
        print('Text is not one')
func('Jeejee', '1') # If you want to change the second parameter,
                    # the first one needs to be changed also

# Try and except statements
text = input('Username: ')
try:
    number = int(text)
    print(number)
except:
    print('Invalid username')

# Global vs local variables
var = 9
loop = True

def func(x):
    global loop # This global keyword changes the global variable
    loop = 7

    if x == 5:
        return newVar
func(2)
print(loop)

# Introduction to objects
x = 5
y = 'string'

def func(x):
    return x+1

print(y.replace('s', ''))
print(func(x))
print(type(x))
print(type(y))

# Creating classes
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('I am', self.name, 'and I am', self.age, 'years old')
    
    def change_age(self, age):
        self.age = age 
        
    def agg_weight(self, weight):
        self.weight = weight
        
jaakko = Dog('Jaakko', 28)
jaakko.speak()
jaakko.change_age(29)
jaakko.agg_weight(95)
print(jaakko.weight)

# Inheritance
# Example 1
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('I am', self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('Bark!')
        
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def talk(self):
        print('Meow!')

jaakko = Cat('Jaakko', 5, 'blue')
jaakko.speak()
jaakko.talk()

# Example 2
class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color
        
    def fillUpTank(self):
        self.gas = 100
        
    def emptyTank(self):
        self.gas = 0
        
    def gasLeft(self):
        return self.gas
    
class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
        
    def beep(self):
        print('beep beep')
        
class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
            
    def beep(self):
        print('honk honk')

rekka = Truck(100, 10, 'green', 'jee')
rekka.beep()

# Overloading methods
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __len__(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.__len__() > p.__len__()

    def __ge__(self, p):
        return self.__len__() >= p.__len__()

    def __lt__(self, p):
        return self.__len__() < p.__len__()

    def __le__(self, p):
        return self.__len__() <= p.__len__()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3

print(p5, p6, p7)

# Static methods and class methods
class Dog:
    dogs = []
    
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
        
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _n in range(n):
            print('Bark!')

koira = Dog('Hauva')

koira.bark(4)
Dog.bark(4)

koira.num_dogs()
Dog.num_dogs()

# Private and public classes
# _ in front of the class or method indicates that it is private

# Optional parameters
def func(word, freq = 3):
    print(word*freq)

call = func('Jee')
call = func('Jee', 5)

# Map function
li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func,li)))

# List comprehension
print([func(x) for x in li])
print([func(x) for x in li if x%2==0])

# Filter function
def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(isOdd, a))
c = list(map(add7, b))

# Lambda function
# Example 1
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 10
func3 = lambda x, y=5: x+y

print(func(2))
print(func3(10))

# Example 2
a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x: x+5, a))
print(newList)

newList2 = list(filter(lambda x: x%2 == 0, a))
print(newList2)

# Collections: Counter
# Example 1
from collections import Counter
c = Counter('gallad')
print(c)
c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)
c = Counter({'a':1, 'b':2})
print(c)
c = Counter(cats=2, dogs=7)
print(c)

print(list(c.elements()))
c.most_common(1)

# Example 2
c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']

c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)

# Example 3
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])
print(c+d)
print(c-d)
print(c&d)
print(c|d)

# Collections: Named tuple
from collections import namedtuple
Point = namedtuple('Point', 'x y z')

newP = Point(3,4,5)
print(newP)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())
print(newP._fields)

newP = newP._replace(y=6)
print(newP)

p2 = Point._make(['a', 'b', 'c'])
print(p2)

# Collections: Deque
from collections import deque
d = deque('Hello')
d.append('4')
d.append(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)

d.extend('456')
print(d)
d.extendleft('123')
print(d)

d.rotate(-1)
print(d)

d = deque('hello', maxlen=5)
print(d)
d.append(1)
print(d)


