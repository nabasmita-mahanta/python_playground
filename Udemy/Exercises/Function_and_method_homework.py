''' Write a function that computes the volume of a sphere given its radius.
The volume of a sphere is given as
4/3π𝑟3
'''


def vol(rad):
    pi = 3.14
    result = (4 / 3) * (pi) * (rad ** 3)
    return result


print(vol(2))

''' Write a function that checks whether a number is 
in a given range (inclusive of high and low)
'''


def ran_check(num, low, high):
    if num in range(low, high + 1):
        return True
        # print(f'{num} is in the range between {low} and {high}')


print(ran_check(3, 1, 10))

'''Write a Python function that accepts a string and calculates 
the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
'''


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

'''Write a Python function that takes a list and returns 
a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''


def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# another way

def uni_list(xyz):
    seen_numbers = []
    for num in xyz:
        if num not in seen_numbers:
            seen_numbers.append(num)
    return seen_numbers


print(uni_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

'''Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24'''


def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total


print(multiply([1, 2, 3, -4]))

'''Write a Python function that checks whether a word or phrase 
is palindrome or not.'''


def palindrome(s):
    if s[:] == s[::-1]:
        return True
    else:
        return False


print(palindrome('helleh'))

'''Hard:
Write a Python function to check whether a string is pangram or not. 
(Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of 
the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons'''
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    # create a set of alphabet
    alphaset = set(alphabet)
    # Remove any spaces from the input string
    str1 = str1.replace(' ', '')
    # Covert into all lowercase.
    str1 = str1.lower()
    # Grab all unique letters from the string set()
    str1 = set(str1)
    # alphabet set == string set input
    return str1 == alphaset


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(string.ascii_lowercase)


