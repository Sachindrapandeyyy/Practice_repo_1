def duplicate(list):
    
    newlist = []
    
    for x in list :
        if x not in newlist :
            newlist.append(x)
    return newlist

x= list(input("enter list ot check duplicate : ").split())
print(duplicate(x))