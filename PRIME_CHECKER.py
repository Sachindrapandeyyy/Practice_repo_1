import random

# Function: Miller–Rabin Primality Test
def is_prime(n, k=10):  # k = number of accuracy iterations
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Step 1: write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Step 2: test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # (a^d) % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Your huge number:
n = int(input("enter a number : "))

# Check primality
if is_prime(n):
    print("✅ The number is probably PRIME.")
else:
    print("❌ The number is COMPOSITE.")
