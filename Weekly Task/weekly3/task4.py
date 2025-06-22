num=int(input("Enter a number : "))
arm=num
sum=0
count = len(str(num))
while num>0:
    digit=num%10
    num=num//10
    sum+=digit**count
if(sum==arm):
    print(arm,"is armstrong")
else:
    print("not armstrong")