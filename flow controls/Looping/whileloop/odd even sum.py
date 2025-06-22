low = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
sumodd=0
sumeven=0
while(low<=upper):
    if(low%2==0):
        sumeven+=low
    else:
        sumodd+=low
    low+=1

print("sum is",sumeven)
print("sum is",sumodd)