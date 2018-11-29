#Design a function within a Python script that takes in a list of numbers,
#for example[1,2,3,4,5]and returns another list with each number multiplied by 2.
#One possible idea/solution looks like:

#     def multiply_by_two(a_list): 
#         values_to_return = []     # put your code and logic here     
#         return values_to_return 

#Running your code: If you want to try out answers, you can print (in the same file),
#example: x = [1,3,5] print(multiply_by_two(x))

def dublicate(numbers): # function that take a list of numbers as an input and return
                        # a new list with the numbers multiplied by 2 as output.
    result = [] #create a new empty list
    for number in numbers:
        result.append(number * 2)
    return result


numbers = [2, 6, 3, 5, 10]
dublicated_numbers = dublicate(numbers)
print(dublicated_numbers)
