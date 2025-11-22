def second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements."
    
    first = second = float('-inf')  # very small initial values
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:  # strictly between
            second = num
    
    # Edge case: all numbers same
    if second == float('-inf'):
        return "No second largest (all numbers are same)"
    
    return second


# Example use
nums = [10, 20, 4, 45, 99]
print("Second largest:", second_largest(nums))
