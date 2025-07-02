f=open('C:/Users/m/Pictures/sample4.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    loc = data[5]

    # age>23
    if age>'23':
        print(data)

    # age equal to 21 fname,lname,age,ph no
    if age=='21':
        print(data[1:5])

    # location equal to chennai fname,lname,age
    if loc=='Chennai':
        print(data[1:4])

    # location equal to chennai and age greater than 23 fname ,lname,age
    if age>'23' and loc=='Chennai':
        print(data[1:5])


