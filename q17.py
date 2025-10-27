def fseries(n):
    series = [0,1]
    
    if n<=0:
        return []
    elif n ==1:
        return[0]
    
    
    for i in range(2,n):
        next_num = series[-1] + series [-2]
        series.append(next_num)
    return series

x = int(input("enter the number of terms for the series "))
print(fseries(x))