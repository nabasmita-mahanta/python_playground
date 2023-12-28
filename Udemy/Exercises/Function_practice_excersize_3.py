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

