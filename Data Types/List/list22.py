string="luminartechnolab"
vowels="aeiouAEIOU"
lst=[]
for i in string:
    if i not in vowels:
        lst.append(i)
print(lst)
print(len(lst))