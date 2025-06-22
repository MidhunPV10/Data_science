#hcf

def function1(x,y):
    if(x<y):
        smallest=x
    else:
        smallest=y

    for i in range(1,smallest+1):
        if(num1%i==0)&(num2%i==0):
            hcf=i
    return hcf

num1=int(input("enter number1 :"))
num2=int(input("enter number2: "))
print("hcf of numbers is",function1(num1,num2))
