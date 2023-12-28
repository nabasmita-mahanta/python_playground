def my_function():
    print("This is my function")
my_function()

def my_func(name,place):
    print(f"Hello {name}! Are you from {place}?")
my_func("Nabasmita","Assam")

def total_bill(bill,tip = 0.10):
    net_bill = bill+bill*tip
    return net_bill
print(total_bill(5000,2))

#arbitary arguments
#Let's create a simple function my_var_sum() that returns
#the sum of all numbers passed in as argument.However the
#number of arguments could be potentially different each time
#we call the function.

def my_var_sum(*args):
    sum=0
    for arg in args:
        sum = sum+arg
        return sum
my_var_sum(1,2,4,5,6)

# Write a function 'digits' that takes a number
# and prints digits of that number
# eg digits(6475)
def digits(x):
    for num in x:
        print(int(x))


# OUTPUT
# 6
# 4
# 7
# 5


