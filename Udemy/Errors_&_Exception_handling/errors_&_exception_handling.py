# We use these three for exception handling:
# TRY : This is the block of code to be attempted ( may lead to an error)
# EXCEPT : Block of code will execute in case there is an error in TRY block.
# FINALLY : A final block of code to be executed, regardless of an error


try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except:
    print("Hey it's looks like you aren't adding correctly")
else:
    print("Add went well")
    print(result)




try :
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")






