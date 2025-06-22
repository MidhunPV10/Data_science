collection=[1,2,3]
for i in collection:
    for j in collection:
        for k in collection:
            if i!=j and j!=k and k!=i:
                print(i,j,k)
