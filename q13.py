#list = list((input("enter a list of numbers ")).split())  use this to take input like this 
#['sachin', 'sachin', '12341241', 'harsh', 'king']
#this will give input like this  ['s', 'a', 'c', 'h', 'i', 'n', ' ', '1', '2', '3', ' ', '4', '4', ' ', '#', ' ']
# list = list((input("enter a list of numbers "))) 
my_list = list((input("enter a list of numbers ")).split())

reversed_list = []

for i in my_list:
    reversed_list.insert(0,i)
print("original list : " , my_list )
print("reveresed_list:", reversed_list)