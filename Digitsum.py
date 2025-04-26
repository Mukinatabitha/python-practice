def Digitsum(number):
    total = 0  # Start with 0
    while number > 0:  # Keep going while there's digits left
        digit = number % 10  # Get the last digit
        total = total + digit  # Add it to total
        number = number // 10  # Remove the last digit
    return total
#trial
print(Digitsum(123))  # Should print 6 (1 + 2 + 3)
