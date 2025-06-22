#calculate electricity bill
#<=100 amount is free
#101 to 200

unit=int(input("Enter the used unit : "))
if(unit<=100):
    Amount=0
elif(unit<=200):
    Amount=(unit-100)*5
else:
    Amount=(unit-200)*10+500
print("Total amount is",Amount)


