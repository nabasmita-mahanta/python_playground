# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            x = int(input("Please enter a number: "))
            y = x ** 2
            print(y)
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print(f'Thank you, your number squared is: {y}')
            break
ask()











