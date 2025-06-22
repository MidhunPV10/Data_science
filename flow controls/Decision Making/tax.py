# calculate road tax

price=int(input("Enter price of the bike:"))
if(price>=100000):
    tax=(price*15)/100
    print("tax amount is",tax)
elif(price>=50000):
    tax=(price*10)/100
    print("tax amount is",tax)
else:
    tax=(price*5)/100
    print("tax amount is",tax)
