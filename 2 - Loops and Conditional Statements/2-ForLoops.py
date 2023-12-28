print("Range Function")
print(range(10)) #(0, 10)
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 12, 2))) #[5, 7, 9, 11]
print()

print("For Loops")
print("Question 1")
for i in range(10):
    print(2*i)

print("Question 2")
for i in range(10):
    print(2*i, end=" ")
print("\n")

print("Question 3")
a = ["Urjani", "Chakravarti", "Aryan", "Bansal"]
for name in a:
    print(name, name*4, end = " ")


