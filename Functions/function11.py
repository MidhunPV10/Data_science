#take the count of the numbers


def myfunction(x):
    count=0
    while(x>0):
        x=x//10
        count+=1
    return count
num=int(input("Enter a number : "))
print("count is",myfunction(num))

