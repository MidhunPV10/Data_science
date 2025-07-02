f=open('fruits','r')
v=open('fruit1','w')
for i in f:
    if "apple" not in i:
        v.write(i)

