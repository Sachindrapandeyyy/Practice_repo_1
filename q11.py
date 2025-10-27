no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

if op =='+':
    result = no1 + no2
elif op =='-':
    result = no1 - no2
elif op =='*':
    result = no1 * no2
elif op =='/':
    
    if no2 ==0 or no1 ==0:
        result = "Error: Division by zero is not allowed."
    else:
        result = no1 / no2
else:
    result = "Error: Invalid operation."
    
print("The result is:", result)
