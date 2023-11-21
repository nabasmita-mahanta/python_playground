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


# Find out average marks scored in subject SQL?
# Extracted col= name with SQL_data=marks
# Extracted only SQL_data=marks
# mathematical operation
student_marks = [['Name',['Statistics','Python','SQL','ML','DeepLearning']],
                 ['Ananya',[41, 34, 45, 55, 63]],
                 ['Akash',[42, 23, 34, 44, 53]],
                 ['Rahul',[32, 23, 13, 54, 67]],
                 ['Gyan',[23, 82, 23, 63, 34]],
                 ['Pranav',[21, 23, 25, 56, 56]] ]
total_sql_marks = 0
total_student = 0
for element in student_marks[1:]:
    sql_marks = element[1][2]
    total_sql_marks = total_sql_marks + int(sql_marks)
    total_student = total_student + 1

average_marks_in_sql = total_sql_marks/ total_student
print(average_marks_in_sql)