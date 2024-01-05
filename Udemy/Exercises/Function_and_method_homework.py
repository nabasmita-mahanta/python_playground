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
