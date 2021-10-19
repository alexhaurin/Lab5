namePrompt = "What's your name?: "
name = str("")

# Get name
while (True):
    try:
        name = str(input(namePrompt))
        print("Hello, " + name + "!")
        break
    except:
        print("Enter a valid input")

# Get other input

# Do stuff
