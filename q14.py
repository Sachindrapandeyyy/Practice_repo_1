import math 

n = int(input("Enter a number to find prime: "))

if n<=1:
    print("yuor given number is not prime ")
else :
    isprime = True
    

    for i in range(2,int(math.sqrt(n)+1)):
        if n % 2 == 0:
            isprime = False
            break
    if isprime:
        print(n,"is a prime number")
    else :
        print(n, "is not prime ")