def new_func():
    print("Hello World")


new_func()


def new_string(string):
    print(string)


new_string('hkjkhjkl')


def user_input():
    # print(input("Enter your name: "))
    pass


user_input()


def string1(string):
    final_string = ""
    for index, letter in enumerate(string):
        if index % 2 != 0:
            final_string = final_string + letter.upper()
            # print(letter.upper(), index)
        else:
            final_string = final_string + letter.lower()
    return final_string


result = string1("Anthropomorphism")
print(result)

