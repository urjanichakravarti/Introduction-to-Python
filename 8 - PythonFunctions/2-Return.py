def sum_of_list(a):
    return(sum(a))

a = (4, 6, 7, 8, 2, 8, 1, 0)
print(sum_of_list(a))
print("\n")

print("Q: Write a function that takes a list of names as an argument and greets hello to everyone")
def greet(nameList):
    for name in nameList:
        print ("Hello", name, "!!!")

names = ("Urjani", "Jayani", "Debaleena", "Surajit")
greet(names)