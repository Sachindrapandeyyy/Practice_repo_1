def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return  n * factorial(n -1)

Number= int(input("Enter a number to find its factorial: "))


if Number < 0:
    print("negative number factorial ni hota hai ")
else:
    Result = (factorial(Number))
print("factorial of the number is ", Result)    