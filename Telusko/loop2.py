import math


def isPerfectSquare(num):
    sqrt = str(math.sqrt(num))
    tokens = sqrt.split(".")
    values_after_dot = tokens[1]
    if (values_after_dot == "0"):
        return True
    else:
        return False


for num in range(1, 500):
    if (isPerfectSquare(num)):
        print(num)
