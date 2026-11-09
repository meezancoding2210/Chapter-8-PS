#Write a Python program to print the first n lines of the following pattern, For n = 3. 
'''
***
**
*
'''


def pattern(n):
    for i in range(1,n+1):
        print("*"*(4-i))


a = int(input("Enter the number: "))
pattern(a)

