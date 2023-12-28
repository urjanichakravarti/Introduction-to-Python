'''
-- In a set, all the elements are unique, ie, elements cannot repeat
-- We use curly brackets to make sets {}
-- Indexing is not supported in sets; elements are in random order
'''

a = {3, 2, 3, 4, 3, 2, 2, 4, 3, 4, 1}
print(a) # {1, 2, 3, 4}

for element in a:
    print(element*3)

arr = [3, 4, 9, 9, 9, 8, 7, 9]
carry = 1
for i in range(len(arr)-1, -1, -1):

    print(arr[i])

    if arr[i] + carry == 10:
        arr[i] = 0
        carry = 1
    else:
        arr[i] += carry
        carry = 0

if carry != 0:
    arr.insert(0, carry)

print(arr)

set1 = set()
set1.add(1)