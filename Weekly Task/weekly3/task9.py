num=int(input("Enter a number : "))
count=0
while num>0:
    digit=num%10
    num=num//10
    count+=1
print("Total number of digits in number is : ",count)