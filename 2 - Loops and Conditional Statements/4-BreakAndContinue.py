print("Question 1")
for i in range(10):
    if i>6:
        break
    print(i)

print("Question 2")
for i in range(10):
    if i == 8:
        continue
    print(i)

a = [1, 2, 1, 1, 1, 2, 3, 4]
print(a.pop())
print(a)