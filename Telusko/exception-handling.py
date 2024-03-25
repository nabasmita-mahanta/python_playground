import sys

while True:
    num = input("Enter your number to divide : ")
    num2 = input("divide by : ")

    try:
        result = int(num) / int(num2)
        print(f'Result is: {result}')
        break
    except ValueError:
        print("Please give a number")
    except ZeroDivisionError:
        print("Cannot divide a number by 0 !! IDIOT")
    except:
        print("Oops !! Something went wrrooongg !! Please try again")

