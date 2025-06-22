low=int(input("Enter lower limit:"))
upper=int(input("Enter upper number:"))
even_sum=0
odd_sum=0
for i in range(low,upper+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i

print("sum of even numbers is ",even_sum)
print("sum of odd numbers is",odd_sum)
