# meraki q1.
# a = {(1,2):1,(2,3):2}    #1
# print(a[1,2])

# meraki q2
# a = {'a':1,'b':2,'c':3}     # keyerror
# print (a['a','b'])

# meraki q3.

# fruit = {}
# def addone(index):
#     if index in fruit:         # 3
#         fruit[index] += 1       # {'Apple':2, 'Banana':1, 'apple':1}
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)

# meraki q4
# Student = {}
# Age = {}                            #1
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"]))

# meraki q5.
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)


#meraki q6.
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates[box]))

# merakij q7.
rec = {                      # True
"Name" : "Python",
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
id1 = id(rec)
del rec
rec = {
    "Name" : "Python", 
    "Age":"20", 
    "Addr" : "NJ", 
    "Country" : "USA"
    }
id2 = id(rec)
print(id1 == id2)

