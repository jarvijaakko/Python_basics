# Catching up with some Python basics first time in a long time

# Inputting strings
# print('Give me your name:')
# name = input()
# print('Hello', name)

# Operators
# print('Pick a number: ')
# num1 = input()
# print('Pick another number: ')
# num2 = input()
# 
# sum = int(num1) + int(num2)
# 
# print(sum)

# print(num1/num2) # Division
# print(num1**num2) # Power
# print(num1//num2) # Integer division
# print(num1%num2) # Modulus

# Conditions (<>)
# print(4 != 5)

# If/else
# print('How old are you? ')
# age = input()
# 
# if int(age) >= 18:
#     print('You are an adult')
# else:
#     print('You are a child')
# 
# Chained conditionals (and, or, not)
# print('How old are you? ')
# age = input()
# 
# if int(age) >= 18:
#     print('You are an adult')
# elif (int(age) >= 15) and (int(age) < 18):
#     print('You are a teenager')
# else:
#     print('You are a child')

# Nested statements
# x = 2
# y = 3
# if x == 2:
#     if y == 3:
#         print('x = 2 and y = 3')
#     else:
#         print('x = 2 but y != 3')
# else:
#     print('x != 2')

# For loops
# for x in range(0, 10, 1): # (start, stop, step)
#     print(x)

# While loops
# loop = True
# 
# while loop:
#     password = input('Enter password: ')
#     if password == 'salasana':
#         break
#         
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



