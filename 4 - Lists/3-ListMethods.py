'''
List Methods
-- append
-- insert
-- sort
-- pop
-- clear
-- reverse
-- index
-- count
'''

a = [1,2,3]
a.append(4)
print(a)
a.insert(1, 0.5)
print(a)
a = [8,4,8,1,9,2,6]
a.sort()
print(a)
a.pop(0)
print(a)
a.clear()
fruits = ["Apple", "Banana", "Guava"]
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index("Banana"))
print(fruits.count("Apple"))

arr = [1, 2, 3, 4, 5, 6, 7]
arr[2:4] = reversed(arr[2:4])
print(arr)

b = []
sum = 0

a = [1, 4, 45, 6, 0, 19]
x = 51
for i in a:

    sum += i
    b.append(sum)

    if sum >= x:
        break

print(sum)
for i in range(len(b)):
    if b[i] < x - sum:
        b.pop(i)
    else:
        break

print(len(b))
