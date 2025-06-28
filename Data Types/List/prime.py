lst=[1,2,3,4,5,6,7,8,9,10,11,12,13]
lst1=[]

for i in lst:
    if i>1:
        flag = 0
        for j in range(2,i):
            if i%j==0:
                flag=1

        if flag==0:
            lst1.append(i)
print(lst1)