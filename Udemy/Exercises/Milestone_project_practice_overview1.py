# INTRODUCTION TO WARMUP PROJECT EXERCISE

print([1, 2, 3])

print([1, 2, 3])
print([4, 5, 6])
print([7, 8, 9])

# DISPLAYING INFORMATION
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
display(row1, row2, row3)
row2[1] = 'X'
display(row1, row2, row3)


# ACCEPTING USER INPUT

result = input('Please enter a value: ')
print(result)

position_index = int(input("Choose an index position: "))
print(type(position_index))

# VALIDATING USER INPUT
def user_choice():
    # Variabes

    # Initial
    choice = "WRONG"
    acceptable_range = range(0, 11)
    within_range = False

    # Two conditions to check
    # DIGIT or WITHIN_RANGE == FALSE
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry! that's not a digit!")

        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range(0-10)")
                within_range = False

    return int(choice)


print(user_choice())
