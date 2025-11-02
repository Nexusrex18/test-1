# Welcome to the most broken program ever

import math

print("Starting Program...") # missing parenthesis fixed

name = input("What is your name?")    # missing closing parenthesis, indentation errors coming!! fixed

if name =="Bob":
   print("Hey Bob!")
else:
    print("Hello " + name)

numbers = [10, 5, 0, 8]
total = 0

for n in numbers:
    total += n  # using number as index incorrectly

print(f"Total is: {total}")  # string + int error

def divide(a, b):
    try:
        return a / b # indentation error
    except ZeroDivisionError as e:
        return e

print(divide(10, 0))  # division by zero

d = {}
d["age"] = 20
print(d["age"])  # key doesn't exist

class Person
    def __init__(self, name, age)
        self.name = name   # variable typo
        self.age = age

    def speak(self)
        print(f"Hi I'm {self.name} and I am {self.age} years old")  # str + int error fixed

p = Person(name,20)  # wrong constructor usage
p.speak()  # wrong method name

print("Program done!")
