'''
-- all() - returns true if all keys are true; if dict is empty
-- any() - returns true is any key is true; returns false if dict is empty
-- len()
-- sorted()
-- clear()
-- keys()
-- values()
'''

dict = {"Susan": 89, "Sneha": 88, "Medha": 67, "Reshma": 55, "Ananya": 78, "Meenakshi": 88}
dict2 = {"Susan": 89, "Sneha": 88, "Medha": 67, "Reshma": 55, "Ananya": 78, "Meenakshi": 88}
print(all(dict))
print(any(dict))
print(len(dict))
print(sorted(dict))
print(dict.keys())
print(dict.values())
print(dict == dict2)
# print(dict.clear())

map = {}
# arr = [1, 2, 3, 4, 6, 1, 2 , 3, 3 , 3, 3, 4 , 4, 4, 5 , 1, 4,2 , 4]
arr = "{[{{{{{((()))()(}}{}{}{}{][])()()}))}}}}}]"
for i in arr:
    if i in map:
        map[i] = map[i] + 1
    else:
        map[i] = 1
print(map)

if (map['{'] == map['}'] and map['('] == map[')'] and map['['] == map[']']):
    print("balanced")
else:
    print("not balanced")

print(len(map))
