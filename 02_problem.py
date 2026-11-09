#Write a Python program using functions to convert Celsius to Fahrenheit. 

def celtofar(cel):
    faren = (cel*(9/5)) + 32
    return faren

a = int(input("Enter the temperature in Celsius Degree : "))
celtofar(a)
print(f"{a}°C is {celtofar(a)}°F")