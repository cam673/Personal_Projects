#Two Sum

#Find two numbers that match the target value

def two_sum(numbers, target):
    test = 0
    i = 0
    j = 1
    verify = False
    
    #When two numbers are found, return the index positions
    while(i < (len(numbers) - 1)):
        while(j < len(numbers)):
            test = numbers[i] + numbers[j]
            
            if(test == target):
                verify = True
                print("[" + str(i) + ", " + str(j) + "]")
            
            j += 1
        i += 1
        j = i + 1
    
    #Return if no matches were found
    if(verify is False):
        print("[0, 0]")
    
numbers1 = [5, 1, 6, 7, 2]
numbers2 = [3, 8, 10, 1]
numbers3 = [5, 1, 3]

target1 = 13
target2 = 18
target3 = 6

two_sum(numbers1, target1)
two_sum(numbers1, target2)
two_sum(numbers2, target2)
two_sum(numbers3, target3)