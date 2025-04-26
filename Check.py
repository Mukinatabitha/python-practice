def Check(number):
    if number % 2 == 0:  # If remainder is 0, it's even
        return "Even"
    else:  # Otherwise, it's odd
        return "Odd"
#trial
print(Check(5))  # Should print "Odd"

