#   armstrong number between a limit

low=int(input("Enter the lower limit :"))
upp=int(input("Enter the upper limit :"))

for i in range(low,upp+1):
    count=0
    sum=0
    temp=i
    num=temp



    while(num>0):
        num=num//10
        count+=1
    while(temp>0):
        digit=temp%10
        temp=temp//10
        sum+=digit**count


    if(sum==i):
          print(i)
else:
    print("no armstrong numbers")




