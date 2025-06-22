list1=[]
list2=[]
list3=[]
for i in range(1,101):
    list1.append(i)
    if(i%2==0):
        list2.append(i)
    else:
        list3.append(i)
print(list1)
print(list2)
print(list3)
print(sum(list1))
print(sum(list2))
print(sum(list3))