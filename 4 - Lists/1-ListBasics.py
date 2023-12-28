'''
- Lists are created by placing all the elements inside a square bracket[] separated by commas
- They can have any number of elements and elements can have diff data types
- Lists are mutable
Ex: [1, 1.2, "string", False]
'''

list =["okay", 1 , 4+4j, False]
list[0] = "nope"
print(list)

print(list[1])
print(list[-1])

print("Deleting")
del list[3]
print(list)
