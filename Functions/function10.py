#lcm
def checking():
    if(num1>num2):
        return num1
    else:
        return num2

def finding():
    greatest = checking()
    while True:
       if(greatest%num1==0)&(greatest%num2==0):
          return greatest

       greatest+=1



num1=int(input("enter number1 : "))
num2=int(input("enter number2 : "))
lcm=finding()
print("lcm of numbers is",lcm)