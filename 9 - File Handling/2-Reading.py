with open('data.txt', 'r') as f:
    print(f.read())

with open('data.txt', 'r') as f:
    print(f.read(10)) #prints first 10 characters
    print(f.read(10)) #cursor is always maintained, so the next 10 characters are maintained

with open('data.txt', 'r') as f:
    print(f.read(10))
    #in order to put the cursor at a particular location we use seek function
    f.seek(0)
    print(f.read(10))