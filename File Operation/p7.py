#1.rating above 4 movies name,year,rating
#2.below 2000 name,year,duration
#3. each year release movie count
#4. release year above 2005 and rating above 4 name,year,rating
#5. A alphabets movies collect

f=open("C:/Users/m/Pictures/movies_cleaned_pandas.csv",'r')
dic = {}
for i in f:
    data=i.rstrip('\n').split(',')


    # if data[3]>'4':
    #     print(data[1:4])

    # if data[2]<'2000':
    #     print(data[1],data[2],data[4])

#     year=data[2]
#     if year not in dic:
#         dic[year]=1
#     else:
#         dic[year]+=1
# for k,v in dic.items():
#     print(k,":",v)

    
