# While Loop

i = 1

while i <= 5:
    print("Telusko", end=" ")
    j = 1
    while j <= 4:
        print("Rocks", end=" ")
        j = j + 1

    i = i + 1
    print()

# Write a code to print all values from 1 to 100.
# Skip the numbers which are divisible by 3 or 5
for num in range(1, 101):
    if num % 3 == 0 or num % 5 == 0:
        pass
    else:
        print(num)

# FOR LOOP
x = 'Nabas'
for i in x:
    print(i)

for i in [3, 4, 'Puku']:
    print(i)

for i in range(11, 21, 2):
    print(i)
for i in range(20, 10, -1):
    print(i)


# Print all the perfect sqr number between 1 and 500


print("Print all the perfect sqr number between 1 and 500")


def squareOf(num):
    return num * num


perfectSq = 1
numInCheck = 2
while (perfectSq < 500):
    print(perfectSq)
    perfectSq = squareOf(numInCheck)
    numInCheck = numInCheck + 1

