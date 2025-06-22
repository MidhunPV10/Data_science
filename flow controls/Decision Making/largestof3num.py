# largest among three numbers

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))
if((num1>num2) & (num1>num3)):
    print("Number1 is greatest")
elif((num2>num1)& (num2>num3)):
    print("Number2 is greatest")
else:
    print("Number3 is greatest")
