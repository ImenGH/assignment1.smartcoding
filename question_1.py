def dublicate(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


numbers = [2, 6, 3, 5, 10]
dublicated_numbers = dublicate(numbers)
print(dublicated_numbers)
