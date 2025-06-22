num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
opr=input("Enter a operator :")
if(opr=="+"):
    result=num1+num2
elif(opr=="-"):
    result=num1-num2
elif(opr=="*"):
    result=num1*num2
elif(opr=="/"):
    if(num2!=0):
         result=num1/num2
    else:
        print("Enter a number greater than zero")
elif(opr=="%"):
    if (num2 != 0):
        result = num1 % num2
    else:
        print("Enter a number greater than zero")

elif(opr=="//"):
    if (num2 != 0):
        result = num1 // num2
    else:
        print("Enter a number greater than zero")
else:
    print("Invalid operator")
print("result is :",result)
