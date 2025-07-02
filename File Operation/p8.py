f=open("C:/Users/m/Pictures/temper.unknown","r")
dic={}
for i in f:
    data = i.rstrip('\n').split(',')
    district=data[0]
    temp=data[1]

    if district not in dic:
        dic[district]=temp
    else:
        old=dic[district]
        if old<temp:
            dic[district]=temp
        else:
            dic[district]=old
for k,v in dic.items():
    print(k, ":", v)
