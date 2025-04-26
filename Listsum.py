def Listsum(numbers):
    total = 0  # Start with 0
    for num in numbers:  # Go through each number in the list
        total = total + num  # Add the number to total
    return total  # Give back the final total
#trial
print(Listsum([1, 2, 3, 4]))  # Should print 10
