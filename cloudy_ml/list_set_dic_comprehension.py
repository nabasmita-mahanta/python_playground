# Find the element in a list in which elements are ended with
#letter 'b'and the length of the element is greater than 2

names = ['ah','Bh', 'Fd', 'acdb', 'cb', 'Tb','Yd','Chb','Tdb']
new_names = []
for letters in names:
    if letters.endswith('b') and len(letters)>2:
        new_names.append(letters)
print(new_names)

new_names1= [ letters for letters in names if letters.endswith('b') and len(letters)>2]
print(new_names1)

# Given a list of numbers, display the numbers in the form of
# '1= odd','2=even' respectively for odd and even numbers.
nums = [3,10,4,5,7,6]
odd_even_list=[]
for numbers in nums:
    if numbers%2 == 0:
        odd_even_list.append(str(numbers) + ' = Even')
    else:
        odd_even_list.append(str(numbers) + ' = Odd')
print(odd_even_list)

odd_even_list1 = [str(numbers) + ' = Even' if numbers%2 == 0 else str(numbers) + ' = Odd' for numbers in nums]
print(odd_even_list1)


