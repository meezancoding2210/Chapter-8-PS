#Write a program using functions to find the greatest of three numbers. 



def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n3):
        return n2
    else:
        return n3



a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
print("Greatest is :", greatest(a,b,c))