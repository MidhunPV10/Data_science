f=open('C:/Users/m/Pictures/customer1.txt','r')
dic={}
dic = {}
for i in f:
    data = i.rstrip('\n').split(',')
    prof=data[4]
    age=data[3]

    # to find maximum age in each profession
    if prof not in dic:
        dic[prof]=age
    else:
        old=dic[prof]
        if old<age:
            dic[prof]=age
        else:
            dic[prof]=old
for k,v in dic.items():
    print(k,":",v)

    # to find minimum age in each profession
    if  prof not in dic:
        dic[prof]=age
    else:
        old=dic[prof]
        if old > age:
            dic[prof]=age
        else:
            dic[prof]=old
for k,v in dic.items():
    print(k,":",v)
