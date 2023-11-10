def my_function():
    print('Hello')
my_function()

def greet_user(name,age=50):
    print('hello ' + name)
    print('you are '+str(age)+' years old')
greet_user("Bipin Mahanta")

def my_function(*kids):
  print("The fourth child is " + kids[3])
my_function("Emil", "Tobias", "Linus","Max","Mary")

def greet_user(name,age):
    print('hello ' + name)
    print('you are '+str(age)+' years old')
greet_user(age=60, name= "Bipin Mahanta")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#return function

def power_of_number(number,power):
    return (number**power)
result = power_of_number(2,3)
print(result)
