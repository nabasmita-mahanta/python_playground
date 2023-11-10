# Q5. Given a string .
# Print the string skipping the letters e and f.

given_string = "fNafbfefasmfeita efeis eafn afmeazfifenfg fpfeeytfhonf fdfefeveflfoefpefefr"
new_string = ''
for letter in given_string:
    if letter == 'e' or letter == 'f':
        pass
    else:
        new_string = new_string + letter
print(new_string)
