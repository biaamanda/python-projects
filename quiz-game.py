print("Welcome to the Quiz Game!")

play = input("Do you want to play? (yes/no) ")

if play.lower() != "yes":
    quit()
    
print("Great! Let's start the quiz.")
score = 0

answer1 = input("What Python function is used to display output on the screen? ").lower()
if answer1 == "print()":
    print("Correct!")
    score += 1
elif answer1 == "print":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer2 = input("What keyword is used to create a loop that runs while a condition is true in Python? ")
if answer2.lower() == "while":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer3 = input("What data type would you use to store a decimal number in Python? ")
if answer3.lower() == "float":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer4 = input("What function is used to get input from the user in Python? ").lower()
if answer4 == "input()":
    print("Correct!")
    score += 1
elif answer4 == "input":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer5 = input("What keyword is used to define a function in Python? ")
if answer5.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("Your final score is: " + str(score) + "/5")

print("Your got " + str((score / 5) * 100) + "%")
