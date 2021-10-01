# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(person['name'])
# print(result)


# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
    # }
# print(person['gender'])
# x=person.get(4)
# y=person.get('age')
# print(x)
# print(y)

# if 23>34:
#     print("yes")
# elif 23<=34:
#     print("no")
# if 23<3:
#     print("nn")
# else:
#     print("t")
# person['sabreena']='4' # we put key inside a [] and use = operator to assign value.. to add to a dictionary
# print(person)


# dic={'name':'subreena','age':'20','place':'kashmir','hobby':'writing'}
# print(dic)
# # dict={}
# print(dic['name'])
# a=dic.get('age')
# print(a)
# dic['calification']='+2'
# print(dic)
# b=dic.pop()
# print(b)

# c={}    # for square of number
# for i in range(1,6):
#     c[i]=i*i
# print(c)


# odd_dic={x:x*x for x in range(11) if x%2==1}
# print(odd_dic)

# c={}    #for odd squares numbers
# for i in range(1,11):
#     if i%2==1:
#         c[i]=i*i
# print(c)

# x={}   #for even number squares
# for i in range(1,10):
#     if i%2==0:
#         x[i]=i*i
# print(x)

# a={1:1,2:4,3:9,4:16} # to iterate a dictionery
# for i in a:
#     print(a[i])

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
# for state in states_capitals:
#         print(state)
#         print(states_capitals[state])


# synonyms={"moutain":"peak","forest":"jungle"}
# print("1.",synonyms["moutain"])

# synonyms["terrain"]="land"
# print("2.",synonyms)

# synonyms.pop("forest")
# print("3.",synonyms)

# def add():
#     print("nikita")
#     def add2():
#         def sub():
#             print("subreena")
#         sub()
#     add2()
# add()

#  Dictionary Methods
# # marks ={'math':1,'english':2,'science':3}
# marks={}.fromkeys(['math','english','science'],1)
# # Output: {'English': 0, 'Math': 0, 'Science': 0}
# # print(marks)

# # for item in marks.items():
# #     print(item)

# # Output: ['English', 'Math', 'Science']
# print(list(sorted(marks.keys())))




# a=[1,2,3,4,5,6,7,8] # output nhi aa raha hai.
# i=0
# b=[]
# while i<len(a):
#     # b=a[i]
#     c=a[i]==a[-i]
#     b.append(c)
#     i=i+1
# print(a)
