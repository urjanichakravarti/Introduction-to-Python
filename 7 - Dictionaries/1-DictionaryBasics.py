'''
-- Python dictionary is an unordered collection of items with a key-value pair
-- You can update elements in a dictionary, ie, dictionaries are mutable
Ex: my_dict = {1: "One", 2: "Two", 3: "Three"}
'''

marks = {"Urjani": 98, "Rita": 88, "Rahul": 77, "Jayani": 100}

print(marks)
print(marks["Jayani"])

for i in marks:
    print(i, "-", marks[i])

marks["Rita"] = 87
print(marks)