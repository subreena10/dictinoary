dict={"name":"Rajiu","marks":56} # program to print 'exist' if the entered key already exist and print 'not exist' if entered key is not already exists.
user=input("Enter ur name: ")
if user in dict:
    print("exist") 
else:
    print("not exists")