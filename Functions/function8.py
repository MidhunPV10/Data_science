def Addition(x,y):
    return x+y
def Subtraction(x,y):
    return x+y
def Multiplication(x,y):
    return x-y
def Division(x,y):
    return x/y

print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

num1=int(input("Enter number1 :"))
num2=int(input("Enter number2 :"))
choice=input("Enter your choice :")
if(choice=="A")|(choice=="a"):
    print("sum of numbers are :",Addition(num1,num2))
elif(choice=="B")|(choice=="b"):
    print("Difference of numbers are",Subtraction(num1,num2))
elif(choice=="C")|(choice=="c"):
    print("Product of numbers are",Multiplication(num1,num2))
elif(choice=="D")|(choice=="d"):
    print("Result of numbers are",Division(num1,num2))
else:
    print("Invalid choice....!")
