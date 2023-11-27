"""
LESSER OF TWO EVENS: Write ae function that returns th
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
    for index,letter in enumerate(string):
        if index == 0 or index == 3:
            # print(letter.upper(),index)
            final_string = final_string + letter.upper()
        else:
            final_string = final_string + letter
            # print(letter,index)
    return final_string

print(old_macdonald('macdonald'))


