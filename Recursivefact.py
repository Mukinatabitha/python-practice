def Recursivefact(n):
    if n == 0 or n == 1:  #stop when n is 0 or 1
        return 1
    return n * Recursivefact(n - 1)  # Call the function again with (n-1)
#trial
print(Recursivefact(5))  # Should print 120
