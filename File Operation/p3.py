f=open('sample3','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print(sum(lst))




#we can use rstrip() for deleting from right side and lstrip() for deleting from left side