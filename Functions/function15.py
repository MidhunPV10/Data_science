num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 : "))

Sum=lambda a,b :a+b
Difference=lambda a,b :a-b
Product=lambda a,b:a*b
Division=lambda a,b :a/b

print("Sum : ",Sum(num1,num2))
print("Difference : ",Difference(num1,num2))
print("Product : ",Product(num1,num2))
print("Division: ",Division(num1,num2))
