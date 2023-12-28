'''
-- In Python, a file operation takes place in the following order:
    1. Open a file [Syntax: open('filename', 'w') default is read/r]
    2. Read/write (perform operation)
    3. Close the file
-- new line (\n) is a character too

Other Modes:
x - open a file for exclusive creation, ie, if file exists the operation fails
a - open for appending at the end of the file without truncating it. Creates a new file if it doesnt exist
t - opens in text mode
b - opens in binary mode
+ - opens a file for updating
'''


f = open('data.txt', 'r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

'''
To avoid forgeting closing the file/ some error coming before the file can be closed we can use with open
'''

with open('data.txt', 'r') as f:
    for line in f:
        print(line)

