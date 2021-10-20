from random import randrange

name = ""
guessCount = 0

# Get name
while (True):
    try:
        name = str(input("What's your name?: "))
        print("Hello, " + name + "!")
        break
    except:
        print("Enter a valid input")

# Get other input
num = int(randrange(100))
print("I am thinking of a number between 1 and 100") # Testing pull requests

while (True):
    try:
        guess = int(input("What is your guess?: "))
        guessCount += 1
        
        if (guess == num):
            print("Nice! You guessed it in " + str(guessCount) + " tries!")
            break
        elif (guess > num):
            print("Lower")
        elif (guess < num):
            print("Higher")
    except:
        print("Please enter an integer!")
