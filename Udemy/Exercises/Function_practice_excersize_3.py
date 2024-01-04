"""
LESSER OF TWO EVENS: Write a function that returns the
lesser of two given numbers if both numbers are even, but returns
the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result


final_result = lesser_of_two_evens(2, 4)
print(final_result)
print(lesser_of_two_evens(3, 4))

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns 
True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""


def animal_crackers(string):
    res = string.split()
    if res[0][0] == res[1][0]:
        return True
    else:
        return False


print(animal_crackers("nocrybaby naba"))

"""
MAKES TWENTY: Given two integers, return True if the sum of the 
integers is 20 or if one of the integers is 20. If not, return False¶
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""


def makes_twenty(x, y):
    if x == 20 or y == 20 or x + y == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))

"""
OLD MACDONALD: Write a function that capitalizes the first and 
fourth letters of a name¶
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
"""


def old_macdonald(string):
    final_string = ""
    for index, letter in enumerate(string):
        if index == 0 or index == 3:
            # print(letter.upper(),index)
            final_string = final_string + letter.upper()
        else:
            final_string = final_string + letter
            # print(letter,index)
    return final_string


print(old_macdonald('macdonald'))

""" MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. 
The .join() method allows you to join together strings in a list with 
some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'
This means if you had a list of words you wanted to 
turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"
"""


def master_yoda(text):
    res = text.split()
    for text in res:
        return " ".join(res[::-1])


print(master_yoda("I am Nabas"))

"""ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True"""

num1 = 100
num2 = 200


def almost_there(n):
    if n in range(num1 - 10, num1 + 11):
        return True
    elif n in range(num2 - 10, num2 + 11):
        return True
    else:
        return False


print(almost_there(209))

'''FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 1, 3]))

'''PAPER DOLL: Given a string, return a string where for every character 
in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''


# for self practice
# sr_new =''
# sr = "hkhkk"
# for l in sr:
#     result = l*3
#     sr_new = sr_new+result
# print(sr_new)


def paper_doll(text):
    final_text = ''
    for letter in text:
        result = letter * 3
        final_text = final_text + result
    print(final_text)


paper_doll('Hello')

'''BLACKJACK: Given three integers between 1 and 11, 
if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''


def blackjack(x, y, z):
    if (x + y + z) <= 21:
        return x + y + z
    elif 11 in (x, y, z) and (x + y + z) > 21:
        return (x + y + z) - 10
    else:
        return "BUST"


print(blackjack(9, 9, 11))

# def blackjack(a,b,c):
#     if sum([a,b,c])<=21:
#         return sum([a,b,c])
#     elif 11 in [a,b,c] and sum([a,b,c]) <=31:
#         return sum([a,b,c])-10
#     else:
#         return "BUST"

# print(blackjack(9, 9, 11))

'''SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and 
extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6,9, 11]) --> 14
summer_69([7,5,8,3,235,6,21,57,6,83,9,11,0,-9,9,12])
'''


def summer_692(arr):
    flag = False
    sum = 0
    for num in arr:
        if num == 6:
            flag = True
        if flag == False:
            sum = sum + num
        if num == 9:
            flag = False
    return sum


# def summer_69(arr):
#     total = 0
#     add = True
#
#     for num in arr:
#         while add:
#             if num != 6:
#                 total = total + num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total


print(summer_692([2, 1, 6, 9, 11]))

'''SPY GAME: Write a function that takes in a list of 
integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
'''


def spy_game(nums):
    code = [0, 0, 7, 'x']
    for i in nums:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 7, 2, 0, 4, 5, 0]))

'''COUNT PRIMES: Write a function that returns the number of 
prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
'''


def count_primes(number):
    prime = []
    for num in range(0, number + 1):
        if num == 0:
            pass
        elif num == 1:
            pass
        elif num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime.append(num)
    print("The prime numbers are:", (prime))
    print("The count of prime numbers are:", (len(prime)))


count_primes(10)


