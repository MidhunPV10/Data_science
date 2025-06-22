low=int(input("Enter lower limit : "))
upper=int(input("Enter upper limit : "))
for i in range(low,upper+1):
    if i<2:
        print(i)
    else:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==1:
            print(i)

