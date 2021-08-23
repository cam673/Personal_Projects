#Search int position

#Search for a number in a sorted list and return it's position
#if it is not there, return the integer position that it would be located at

def index_finder(nums, target):
    #returns the index position that the target number is located in
    i = 0
    while i < len(nums):
        if target == nums[i]:
            return i
        i += 1
    
    #returns the index position it would be located if the target number was in the list
    i = 0
    while i < len(nums):
        if target < nums[i]:
            return i
        i += 1
    
    #return if would be position is at the end of the list
    return i

example1 = [1, 5, 9, 11]
example2 = [3]
example3 = [2, 3, 5]
t1 = 5
t2 = 0
t3 = 4

r1 = index_finder(example1, t1)
r2 = index_finder(example2, t2)
r3 = index_finder(example3, t3)

print(r1)
print(r2)
print(r3)