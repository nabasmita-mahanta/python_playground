"""
Define a function called myfunc that takes in a string,
and returns a matching string where every even letter is uppercase,
and every odd letter is lowercase. Assume that the incoming string
only contains letters, and don't worry about numbers, spaces or punctuation.
The output string can start with either an uppercase or lowercase letter,
so long as letters alternate throughout the string.
Remember, don't run the function, simply provide the definition.
To give an idea what the function would look like when tested:

myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'
Added note: this exercise requires that the function return a string.
 Print statements will not work here.
"""


def myfunc(string):
    final_string = ""
    for index, letter in enumerate(string):
        if index % 2 != 0:
            final_string = final_string + letter.upper()
            # print(letter.upper(), index)
        else:
            final_string = final_string + letter.lower()
    return final_string


result = myfunc("Anthropomorphism")
print(result)


