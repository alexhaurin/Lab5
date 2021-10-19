from random import randrange

name = str("")
guessCount = int(0)

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
print("I am thinking of a number between one and 100")

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
        print("Please enter an integer")
