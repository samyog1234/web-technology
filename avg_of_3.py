"""Making def function named avg"""
def avg():
    """prompt user to enter 3 numbers"""
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    num3=float(input("Enter third number:"))
    """Doing arthemitic operation"""
    avg=(num1+num2+num3)/3
    """printing value of above operation"""
    print("The average of your number is",avg)
"""Returning Function"""
avg()

