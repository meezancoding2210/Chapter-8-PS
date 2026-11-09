#Write a Python function which converts inches to centimeters. 

def inchtocms(inch):
    return inch * 2.54


a = int(input("Enter the length in inches: "))
inchtocms(a)
print(inchtocms(a))