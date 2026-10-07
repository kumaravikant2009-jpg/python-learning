numbers = [10, 5, 8, 20, 15]

largest = second_largest = float('-inf')

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print(second_largest)