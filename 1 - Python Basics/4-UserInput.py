name = input("enter your name: ")
print(type(name))
print("Hello",  name)

a = int(input("Enter var 1: "))
b = int(input("Enter var 2: "))

print(type(a))
print(type(b))
print(a+b)

print("Q: Write a program to take marks of a user in English, Maths and Science and print the avg marks")
marks_eng = int(input("Enter your marks for English: "))
marks_maths = int(input("Enter your marks for Maths: "))
marks_science = int(input("Enter your marks for Science: "))

avg = (marks_maths+marks_eng+marks_science)/3
print("Average Marks = ", avg)