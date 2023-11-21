my_list = [[34, 'Ananya'], [23, 'Akash'], [23, 'Rahul'], [82, 'Mukesh'], [23, 'Pranav']]

res = lambda element: element[0]


def compare_student(element):
    return element[0]


sorted_list = sorted(my_list, key=lambda element: element[0])
print(sorted_list)

highest_marks = 0
highest_name = ''
for element in my_list:
    marks = element[0]
    names = element[1]
    if marks > highest_marks:
        highest_marks = marks
        highest_name = names
print(highest_name)
print(highest_marks)
