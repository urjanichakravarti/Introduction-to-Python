'''
Types of Functions:
-- Built-in functions
-- Modules
-- User defined functions

Built-in Functions:
-- int(), float(), eval()
-- input()
-- min(), max()
-- abs()
-- type()
-- len()
-- round()
-- range()
etc

Module:
-- A module is a file that contains Python code
-- Each module should contain functions that perform related tasks
Important Modules: math, string, random
'''

#Modules
import math as m
print(dir(m))
print(m.pi)
print(m.cos(2.4))

from math import cos, sin, tan as trig
print(trig(2.4))

#User Defined functions
def user_defined_function(name, time_of_day = "morning"):
    print("Hello", name)
    print("Good", time_of_day)

user_defined_function("Urjani")
user_defined_function("Sita", "night")
user_defined_function("Garima", "evening")

str1 = "amazon"

n = len(str1)
res1 = str1[2:]
res2 = str1[:(n - 2)]

for i in range(0, 2):
    res1 = res1 + str1[i]

for i in range(n - 1, n - 3, -1):
    res2 = str1[i] + res2

print(res1)
print(res2)

a = "Hello"
b = "Hell"

print(b in a)

l = [(3, 4), (1, 2), (9, 11), (2, 5)]
l.sort()
print(l)

abc = [1, 2, 3, 4, 1, 1,1]
x = abc.pop()
print(abc)