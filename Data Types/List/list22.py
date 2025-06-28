#[1,6,3,,11,5,15]

lst=[1,3,6,5,4,3,4,6,8,9,10,11,9,7,6,5,6,8,9,15,14,12,11]


result=[lst[0]]
for i in range(1,len(lst)-1):
    if (lst[i-1]<lst[i]>lst[i+1]) or (lst[i-1]>lst[i]<lst[i+1]):
        result.append(lst[i])
print(result)






