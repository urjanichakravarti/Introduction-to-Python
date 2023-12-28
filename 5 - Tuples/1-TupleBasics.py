'''
Intro:
-- Tuples are created by placing elements inside a parenthesis
-- Tuples are immutable

Functions:
-- len(tuple)
-- max(tuple)
-- min(tuple)
-- tuple(seq)
-- sum(tuple)

'''

tup = (2, 3, "Urjani", False, True, "Okay")
print(tup)
print(len(tup))

tup2 =(3, 4, 5, 6, 9, 12)
print(max(tup2))
print(min(tup2))
print(sum(tup2))

str = "urjani_chakravarti"
print(tuple(str))

lst = []
lst.append((1,2))
lst.append((1,3))
print(lst)