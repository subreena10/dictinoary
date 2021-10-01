dic1={1:10, 2:20}  # program to make a single dictionery and add the values having same key.
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic2:
    if key in dic1:
        dic1[key]=dic1[key]+dic2[key]
        dic1.update(dic3)
    else:
        dic1[key]=dic2[key]
print(dic1)


