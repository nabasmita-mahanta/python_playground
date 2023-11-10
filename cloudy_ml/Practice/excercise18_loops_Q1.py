# Q1. Given a list of numbers,
# find weather a given number is present in the list.
numbers = [2, 3, 5, 6, 8, 65, 49, 21]
given_num = 8
number_is_present = False
for item in numbers:
    if item == given_num:
        number_is_present = True

if number_is_present:
    print(str(given_num) + " is present in the list")
else:
    print(str(given_num) + " is not present in the list")
