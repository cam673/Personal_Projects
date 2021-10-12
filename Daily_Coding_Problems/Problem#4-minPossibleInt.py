'''
Daily Coding Problems - #4
Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.
'''
def returnMin(numList):
    accum = 1
    while accum != 0:
        if accum in numList:
            accum += 1
        else:
            return accum

numbers = [3, 4, -1, 1]
result = returnMin(numbers)

print('The result is: ' + str(result))
