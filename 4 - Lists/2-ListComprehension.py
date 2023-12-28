'''
- List comprehension is an elegant way to create a new list from existing list
Syntax: new_list = [expression      for item in list        if condition]
'''

a = [x for x in range(100)]
print(a)

a2 = [x for x in range(10) if x%2==0]
print(a2)

b = [3**i for i in range(10)]
print(b)