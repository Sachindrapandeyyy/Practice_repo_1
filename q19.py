def argams(str1,str2):
    str1.replace(" ","").lower()

    str2.replace(" ","").lower()
    
    return sorted(str1) == sorted(str2) # return Counter(str1) == Counter(str2)  .. can use this also 

#Sorted: It takes any iterable (like a string or list) and returns a sorted list of its elements in ascending order.
#['e', 'i', 'l', 'n', 's', 't']
#Counter : It counts how many times each character (or element) appears.
#Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})

x= str(input("enter a word a sentence  :"))
y= str(input("enter second word or sentence  :"))

if argams(x,y):
    print("hai bhai hai ")
else:
    print("ni hai bhai ni hai ")   