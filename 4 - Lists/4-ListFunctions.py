'''
List Functions
-- len(list)
-- max(list)
-- min(list)
-- list(seq)
-- sum(list)
'''

list1 = [1,3,6,3,4,5,1,8,7,3,10]
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
print(sum(list1[3:7]))
print(sum(list1[:4]))
print(sum(list1[:1]))

s = "urjani"
print(list(s))

A = [1, 3, 5, 2, 2]


def equilibriumPoint(A, N):
    # Your code here

    for i in range(N):
        sumL = sum(A[:i])
        sumR = sum(A[i + 1:])
        if sumL == sumR:
            return sumR

    return -1

print(equilibriumPoint(A, 5))

a = [1, 2, 3, 4, 5, 1]
print(a.index(1))

arr = [15,-2,2,-8,1,7,10,23]

a = [1, 2, -3, 4, 5]

a.sort()
print(a)
i = 0
Sum = sum(a)
print(Sum)
n = 5
k = 1

while i < n - 1 and k != 0:

    if a[i] < 0:
        Sum += a[i]
    else:
        Sum -= a[i]

    i += 1
    k -= 1

print(Sum)



