#Write a recursive function to calculate the sum of the first n natural numbers. 
'''
sum(n) = 1 + 2 + 3 +.. + n
sum(n) = n + n-1 + n-2 + .. + 3 + 2 + 1 
sum (n) = n + sum(n-1)'''

def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1) #so the function keep calling itself.

a = int(input("Enter a number to print n natural numbers: "))
sum(a)
print(sum(a))

