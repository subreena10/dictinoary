my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in range(3):
    max=0
    for j in my_dict:

        if max<my_dict[j]:
            max=my_dict[j]
            b=j
    # a.append(b)
    a.append(my_dict[b])
    my_dict.pop(b)
print(a)
    
    