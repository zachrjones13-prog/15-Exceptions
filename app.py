"""
Exception: what is thrown when an error in your application occurs
crashes your program 

print 4/0
zerodivisonerror: divison by zero

str = "cheese"
if str > 1:
    print(5)
TypeError: '>' not supported between instances of str and int

print(int("A))
valueerror invalid literal for int() with base 10: 'a'

cool function
namerror name coolfunction is not defined

Try: the code block that is potentially dangerous
except the code to run if an exception occurs
Finally: the block fo code that runs after a try except either way

"""
# try:
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("enter the second number: "))
#     print(num1/num2)
# except ZeroDivisionError:
#     print(" cannot divide by zero ")

# except ValueError:
#     print('please enter a valid integer')



try:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    print(num1/num2)
except ValueError:
    print("Inappropriate argument value (of correct type).")
finally:
    print("operation complete")

