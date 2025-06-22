num=int(input("Enter a number:"))
if num<0:
    print("Please enter a positive integer...! ")
elif num==0:
    print("You have entered zero")
elif num==1:
    print("1 is a composite number")
else:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime")
            break
    else:   # this else is paired with the for loop,not the if statement
        print("Number is prime")


