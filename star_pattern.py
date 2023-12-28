for i in range(1, 5):
    for j in range(1, 5):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 5):
    for j in range(1, 8):
        if j <= (5 - i) or j >= (3 + i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)

for num in range(1, 101):
    if num % 3 == 0 and num % 6 != 0:
        print(num)