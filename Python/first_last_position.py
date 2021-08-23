#First and last position

#Find the target number in an ordered list and return it's starting index and ending index
#Return [-1, -1] if the target number was not found

def first_last(nums, target):
    index = 0
    start = 0
    end = 0
    i_found = False
    
    #search for the target's starting index position
    i = 0
    while i < len(nums):
        if nums[i] == target:
            index = i
            i_found = True
            break
        i += 1
    
    #find the last index position that the target is located in and return the result
    if i_found is True:
        result = [index]
        i = index + 1
        while i < len(nums):
            if nums[i] != target:
                break
            if nums[i] == target:
                index = i
            i += 1
        result.append(index)
        return result
    
    #if the target was not found return a list of [-1, -1]
    result = [-1, -1]
    return result

example1 = [1, 3, 4, 5, 5, 5, 5, 5, 7, 10]
example2 = [8, 9, 11]
example3 = [1]
example4 = [2, 2, 3, 6, 6, 7]
t1 = 5
t2 = 10
t3 = 1
t4 = 3

r1 = first_last(example1, t1) # [3, 7] expected result
r2 = first_last(example2, t2) # [-1, -1] expected result
r3 = first_last(example3, t3) # [0, 0] expected result
r4 = first_last(example4, t4) # [2, 2] expected result

print(r1)
print(r2)
print(r3)
print(r4)