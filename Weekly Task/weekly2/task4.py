Age=int(input("Enter your age : "))
Sex=input("Enter your sex(M/F):")
Days=int(input("Enter number of days you worked :"))
if(Age>=18)and(Age<30):
    if(Sex=="M"):
        Wages=700*Days
    elif(Sex=="F"):
        Wages=750*Days
elif(Age>=30)&(Age<=40):
    if(Sex=="M"):
        Wages=800*Days
    elif(Sex=="F"):
        Wages=850*Days
else:
    Wages="not allowed"

print("Your age is",Age,"and your sex is",Sex,".You worked for",Days,"days so you got",Wages,"wages")
