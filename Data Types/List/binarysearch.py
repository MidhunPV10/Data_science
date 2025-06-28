lst=[4,1,3,9,5,8,7,6,2]
element=int(input("Enter a element : "))
lst.sort()
low=0
upper=len(lst)-1
flag=0
while(low<=upper):
    mid=(low+upper)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upper=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag==1):
    print("Element found")
else:
    print("Element not found")







