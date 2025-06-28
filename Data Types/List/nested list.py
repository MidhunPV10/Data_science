lst=[[101,'vinay','p',29,'django',10000],
     [102,'anoop','v',30,'python',12000],
     [103,'vijay','s',34,'mern stack',11000],
     [104,'ajay','r',40,'django',12500],
     [105,'arjun','h',32,'django',12700]]
print(lst)

for i in lst:
    if i[3]==29:
        print(i)

for i in lst:
    if i[3]>29:
        print(i[1:5])

for i in lst:
    if i[4]=="django":
        print(i[1:4])

for i in lst:
    if i[4]=="python":
        print(i[1::2])

for i in lst:
    if i[4]=="django" and i[3]>29:
        print(i[1:4])

# to find total salary
sum=0
for i in lst:
    sum+=i[5]
print(sum)
