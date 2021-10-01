a="MISSISSIPPI"
b={}
i=0
for i in a:
    count=0
    if i not in b.keys():
        for j in a:
            if i==j:
                count+=1
        b[i]=count
print(b)