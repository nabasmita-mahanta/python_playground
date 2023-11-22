student_marks = [['Name', ['Statistics', 'Python', 'SQL', 'ML', 'DeepLearning']],
                 ['Ananya', [41, 34, 45, 55, 63]],
                 ['Akash', [42, 23, 34, 44, 53]],
                 ['Rahul', [32, 23, 13, 54, 67]],
                 ['Gyan', [23, 82, 23, 63, 34]],
                 ['Pranav', [21, 23, 25, 56, 56]]]

maximum_marks_each_subject = 70
number_of_subjects = 5
student_marks_total = []
for element in student_marks[1:]:
    marks = element[1]
    marks.sort(reverse=True)
    name = element[0]
    print('name: ' + name)
    print('marks: ' + str(marks))
    total_marks = 0
    for mark in marks[0:4]:
        total_marks = mark + total_marks

    student_marks_total.append([total_marks, name])

print(student_marks_total)

highest_marks = 0
topper_name = ''

for element in student_marks_total:
    marks = element[0]
    student_name = element[1]

    if marks > highest_marks:
        highest_marks = marks
        topper_name = student_name

topper_percentage = highest_marks * 100 // (number_of_subjects * maximum_marks_each_subject)
print(f'Topper percentage is: {topper_percentage} %  Name is: {topper_name}')
