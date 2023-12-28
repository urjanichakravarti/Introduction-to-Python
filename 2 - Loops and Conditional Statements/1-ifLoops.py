print("Q1: Voter eligibility")
age = int(input("Enter your age: "))
canVote = False
if age >= 18:
    canVote = True

if canVote == True:
    print("You are eligible to vote")
else:
    print("Only 18+ citizens can vote. Try again after", 18-age, "years")

print("Q2: Positive or negative")
num = int(input("Enter the number: "))

if num < 0:
    print("NEGATIVE")
elif num == 0:
    print("ZERO")
else:
    print("POSITIVE")
