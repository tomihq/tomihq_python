#Exceptions and how to handle it.
def divide_by(a, b):
    return a/b

#Program crashes
""" print(divide_by(5, 0)) """

#Program doesn't crash but the error is generic. Show the error code
""" try:
    ans = divide_by(40,0)
except Exception as e:
    print("Something went wrong!", e) """

#Program doesn't crash but the error is generic. Show the class and the error
try:
    ans = divide_by(40,0)
except Exception as e:
    print("Something went wrong!", e)
    print(e.__class__)

#Program doesn't crash, the error is handled with a custom message and if another occurs there is the generic.

try:
    ans = divide_by(40,0)
except ZeroDivisionError as e: 
    print(e, ": We can't divide by zero.")
except Exception as e:
    print("Something went wrong!", e)
    print(e.__class__)


