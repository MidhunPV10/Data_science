#factorial of 2 numbers
num=int(input("Enter a number :"))
i=1
fact=1
while(i<=num):
    fact*=i
    i+=1
print("factorial of number is",fact)