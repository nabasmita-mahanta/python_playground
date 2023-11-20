#using continuation character(\):
sum = 1+2+3+ \
      4+5+6+ \
      7+8+9
print(sum)
#using parentheses():
sum = (1+2+3
       +4+5)
#using sq. brackets[]
#using braces{}

if 10>5:
    print('hello')
    if 5>2:
        print('world')
print('python')

password = "qwert"

for i in range(1, 5):
    user_input = input('Enter Password: ')
    if user_input == password:
        print('Welcome to CloudyML Course!!')
        break
    else:
        print('Wrong Password!!')
        if i == 3:
            print('One Last Trial left!!!')
