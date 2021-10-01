# squares={x:x*x for x in range(1,6)}
# print(squares)

squares={}
for x in range(1,6):   # square of odd numbers.
    if x%2!=0:
        squares[x]=x*x
print(squares)

# def disp():  # function
#     def show():
#         return "show function"
    
#     result=show()  + "  disp function"
#     return result
#     # show()
# # a=disp()
# # print(a)
# print(disp())