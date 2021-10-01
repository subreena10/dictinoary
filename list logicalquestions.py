# user=input("enter ur name: ")   #list vowel consonant in sequence.
# string=list(user) #'s','u',
# vowel=['a','e','i','o','u']
# string.sort()
# for i in string:
#     if i in vowel:
#         print("vowel",i)
#     else:
#         print("consonant",i)

# a=["saloni","subreena","priya","dimplekumari","sonumonikapragapati"]    #list find the maxium namme.
# i=0
# max=a[i]
# for i in a:
#     if len(i)>len(max):
#         max=i
# print(max)


# a=["saloni","subreena","priya","dimple"]              #even odd in list
# i=0
# while i <len(a):
#     if len(a[i]) %2==0:
#         print("even",a[i])
#     else:
#         print("odd",a[i])
#     i+=1

# if False:                 #ifelse logical question.
#     if True:
#         print("56")
# if True:
#     if False:
#         print("76")
# if True:
#     if True:
#         print("78")



# a=[1,2,3]                                 #list
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             c=a[i],a[j],a[k]
#             b.append(c)
#             k+=1
#         j+=1
#     i+=1
# print(b)

# a=[1,2,3]                             #list
# i=0
# b=[]
# for i in range(len(a)):
#     j=0
#     c=[]
#     for j in range(len(a)):
#         if i!=j:
#             c.append(a[i])
#             c.append(a[j])
#         if c not in b:
#             b.append(c)
# print(b)

# list=[[1,2,3],[4,5,6],[7,8,9]]     #indexing of nested list.
# i=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#          print(i,j,list[i][j])
#          j+=1
#     i+=1


# list=[1,2,3,4,5,6,7]           # silicing of list.
# print(list[2:7:2])   

# num=input("enter ur number: ")         #if else logical question.
# b=len(num)-2
# c=int(num)//10**b
# d=c%10
# if d==3:
#     print("yes")
# else:
#     print("no")

# i=1                         #table of 1 to 10.
# while i<=10:
#     j=1
#     while j<=10:
#         product=i*j
#         # print(i," ", "X"'  ,j, " ",  "=",   "  " ,product,   end="  ")
#         print(product," ",end=" ")
#         j+=1
#     print()
#     i=i+1

# i=1                            #table taking from  single user.
# num=int(input("enter a number: "))
# while i<=num:
#     product=num*i
#     print(num,"X",i,"=",product)
#     i+=1


# birthyear=int(input("enter your  birth year: "))         #future age if else.
# futureyear=int(input("Enter year: "))
# age=futureyear-birthyear
# if birthyear<futureyear:
#     print("your future is age ",age)

# else:
#      print("inavlid")


# a=[1,2,3,"9","6",7,10,1.2]    #ina given list find out int,float,str.
# i=0
# b=[]
# c=[]
# d=[]
# while i<len(a):
#     if type (a[i])==str:
#         b.append(a[i])
#     elif type(a[i]) ==float:
#         c.append(a[i])
#     else:
#         if type(a[i])==int:
#             d.append(a[i])
#     i=i+1
# print(b)
# print(c)
# print(d)

# b=[1,2,3,4,[6,7,8]]    # remove []. make a flat list.
# i=0
# a=[]
# while i<len(b):
#     if type(b[i]) is list:
#         j=0
#         while j<len(b[i]):
#             a.append(b[i][j])
#             j+=1
#     else:
#         a.append(b[i])
#     i+=1
# print(a)

# a=[1,2,3,4,5,6,7,8,9,10]    
# i=0
# b=[]
# while i<len(a):
#     if a[i]%3==0:
#         b.append(20)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)


# a=[1,2,4,3,7,9,5,8,10]
# i=0
# while i<len(a):
#     if i%2==0:
#         print(a[i],"even")
#     else:
#         print(a[i],"odd")
#     i+=1


# a="12"
# b="05"
# c="2021"
# print(a+"/"+b+"/"+c)

# a="12hours"
# print(12*2,"hours")

# name="my name is monika"
# print(name.title())

# user=input("enter your name: ")
# dic={}
# for i in user:
#     dic[i]=dic.get(i,5)
# print(dic)


