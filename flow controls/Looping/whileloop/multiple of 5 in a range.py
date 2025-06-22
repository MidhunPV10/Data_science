#lower to upper divisible by 5

low = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
while(low<=upper):
    if(low%5==0):
        print(low)
    low+=1