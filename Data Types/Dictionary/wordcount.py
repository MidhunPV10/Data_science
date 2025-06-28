#wordcount problem is to find  the count of word how much times repeat in a sentence or a paragraph
line='cat dog mango rat cat cat dog bag mango rat rat bat'
#first stage of this problem is to split the line into words using split()function.if we use split ,output will be converted into list
data=line.split(' ')
print(data)
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)

