
try:
    numb1 = int(input("enter the numb1 here: "))
    num2 = int(input("enter the numb2 here: "))
    print(numb1/num2)
except ZeroDivisionError, ValueError:
    print("You cannot divide by Zero!")