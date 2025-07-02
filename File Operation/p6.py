#1.age above 50 fname,lname,age,prof
#2.age range 25 to 40 fname,lname,age,prof
#3.india work fname,lname,age,prof
#4.india work and age above 50 fname,lname,age
#5.uk work fname,lname,age,prof
#6.doctor prof fname,lname,age
#7.doctor and age below 40 fname,lname,age
#pilot prof fname,lname,age
#each prof count
#each location count

f=open('C:/Users/m/Pictures/customer1.txt','r')
dic = {}
for i in f:
    data = i.rstrip('\n').split(',')

    if data[3]>'50':
        print(data[1:5])

    if data[3]>'25' and data[3]<'40':
        print(data[1:5])

    if data[-1]=='india':
        print(data[1:5])

    if data[3]>'50' and data[-1]=='india':
        print(data[1:4])

    if data[-1]=='uk':
        print(data[1:5])

    if data[4]=='Doctor':
        print(data[1:4])

    if data[4]=='Doctor'and data[3]<'40':
        print(data[1:4])

    if data[4]=='Pilot':
        print(data[1:4])

    prof=data[4]

    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
for k,v in dic.items():
        print(k,":",v)

#     loc=data[-1]
#     if loc not in dic:
#         dic[loc]=1
#     else:
#         dic[loc]+=1
# for k,v in dic.items():
#     print(k,":",v)




