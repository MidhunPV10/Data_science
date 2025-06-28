#linear search algorithm

lst=[1,6,9,2,4,10,15,20,12,18,30]
element=int(input("Enter a element : "))
flag=0
for i in lst:
    if i==element:
        flag=1
if flag==1:
    print("Element found")
else:
    print("not found")