#Write a Python function to print the multiplication table of a given number. 

def table(n):
    for i in range(11):
        print(f"{n} x {i} = {n*i}")

a = int(input("Enter a number to find its multiplication table: "))
table(a)