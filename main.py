# #non premitive : list, tuple 
# var : list = ["geeks","for","geeks",2.3,4,True,"geeks","geeks"]
# li3 : list = [1,2,3]
# print(var)
# length = len(var)
# print(length)
# li2 =var[0:7:2]
# print(li2)
# print(var)
# print(li2.pop())
# print(li2)
# #shallow copy : slice copy and deep copy : the copy which change the orignal copy also concept describe above
# print(li2[-1])
# #append
# #insert
# #extent
# var.append(10)#addd value at end of thle list 
# print(var)
# var.insert(1,"ahmed")#if you want to add value at specific index
# print(var)
# var.extend(li3)#it combine the two lists (extent)
# print(var)
# #remove it remove the element in the list it also used to remove the element at a specific value name
# var.remove("geeks")
# print(var)
# #pop() it remove end by default but if specifies index it will work , it also return the value that he remove
# remove_ele = var.pop(0)
# print(remove_ele)
# # #clear() it empty the list
# # var.clear()
# # print(var)
# #delete() it also work for dictionary , lists and for tuples
# del var[3]
# print(var)
# #count it count the specic count value 
# count = var.count("geeks")
# print(count)
# #copy() function it make teh copy of all the list 
# var2 = var.copy()
# print(var2)
# number : list = [1,3,5,6,6,2,2,4]# ascending order
# #sort()
# number.sort()
# print(number)
# number.sort(reverse=True)
# print(number) 
# #index value
# index = number.index(2)
# print(index)
# #maximum and minimum and sum
# max = max(number)
# min = min(number)
# sum = sum(number)
# print(max,min,sum)

# ##tuple : it is immutable : it is not changeable , it has only two functions 
# tu : tuple = (1,2,3,3,4,"hello",True,9.7)
# count = tu.count(3)
# #single value tuple :
# tu1 = (3,)
# print(type(tu1))
#take list input values 
# li = []
# for x in range(3):
#     user_input = int(input("enter any number : "))
#     li.append(user_input)
# print(tuple(li)) #type castng to tuple 
# #nested tuple :
# tu1 = (1,2,3,4)
# tu2 = (1,2,3,4)
# print(tu1+tu2)
# print(tu1 * 3)#1234 jitne bar multipjly karein gay wo utni bar repeat kr de ga 
# #nested tuple 
# tu3 = (tu1,tu2)
# print(tu3)
# #nested list 
# li4 = [1,2,3]
# li5 = [1,]
# li6 = [li4,li5]
# # print(li6)
# #assignment: 
# name = input("enter your name : ")
# education = input("enter your education:")
# roll_no = input("enter your roll number:")
# tuple_values = (1,name,2,education,3,roll_no)
# print("\ntuple:")
# print(tuple_values)
# print("tuple Values:")
# print(f"{tuple_values[0]}: {tuple_values[1]}")
# print(f"{tuple_values[2]}: {tuple_values[3]}")
# print(f"{tuple_values[4]}: {tuple_values[5]}")
# # #assignment 2 :
# li = [33,43,12,45,5]
# sorted_list = sorted(li,reverse=True)
# user_input = int(input("Enter 1 for the highest number or 2 for the second highest number and so on .. :"))
# if user_input == 1:
#     print("The first highest number is:", sorted_list[0])
# elif user_input == 2:
#     print("The second highest number is:", sorted_list[1])
# elif user_input == 3:
#     print("The third highest number is:", sorted_list[2])
# elif user_input == 4:
#     print("The fourth highest number is:", sorted_list[3])
# elif user_input == 5:
#     print("The fifth highest number is:", sorted_list[4])