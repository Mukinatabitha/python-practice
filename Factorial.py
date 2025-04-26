def Factorial(n):
    result = 1  # Start with 1
    for i in range(1, n + 1):  # Go from 1 to n
        result = result * i  # Multiply result with each number
    return result
# trial
print(Factorial(4))  # Should print 24 (4 * 3 * 2 * 1)
