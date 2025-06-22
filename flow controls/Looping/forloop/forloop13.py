low=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
sum=0
for i in range(low,upper+1):
    if(i%2==0):
        sum+=i
print(sum)
