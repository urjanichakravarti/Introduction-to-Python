'''
- Strings are immutable
'''
print("Basics")
name = "Urjani"
multilineString = '''This is
a multiline
string'''
print(name)
print(multilineString)
print("\n")

print("Indexing")
fruit = "Apple"
print(fruit[3])
print(fruit[-1])
print("\n")

print("Slicing")
str = "abcdef"
print(str[1:4]) #[x,y)
print(str[:3])
print(str[1:])
print(str[1:5:2])
print(str) #strings are immutable
print("\n")

print("Reversing")
print(str[::-1])
print("\n")

print("Concatination")
a = "abc"
b = "def"
c = a+b
print(c)
print("\n")

print("Multiplying")
print(c*2)

# emp = []
# print("Empy:", emp.pop())


str = "Urjani"

for i in range(len(str)-1, -1, -1):
    print(str[i])

print(0%2)
