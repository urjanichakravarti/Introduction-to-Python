a = [3,5,8,2,9,4,7]

for element in a:
    print(element*2, end=" ")

s = "the sky is blue"
arr = []
temp = ''

for i in s:

    if i != ' ':
        temp += i
    elif i == ' ' and len(temp) > 0:
        arr.append(temp)
        temp = ''
    print(temp)
