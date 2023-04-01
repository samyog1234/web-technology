"""creating function named name_age"""
def name_age():
    """prompt user to enter their name"""
    name=str(input("Enter your name:"))
    """prompt user to enter their age"""
    age=int(input("Enter your age:"))
    """prompt user to enter their qualification"""
    qualification=str(input("Enter your major qualification in words:"))
    """print the name, age and qualification"""
    print("My name is",name,"and my age is",age,". My major qualification is",qualification)
"""For Returning Function"""
name_age()
