#Add two numbers

#Add two numbers which digits are stored in linked lists

#Definition for a linked list
class linkedlistNode(object):
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

#Add two linked lists
def add_two_numbers(num1, num2):
    remainder = 0
    val1 = 0
    val2 = 0
    newVal = 0
    l1 = num1
    l2 = num2
    prevNode = linkedlistNode(0)
    currNode = linkedlistNode(0)
    result = linkedlistNode(0)
    firstNode = True
    
    #Add values together from the lists
    while True:
        #Add next digits
        val1 = l1.value
        val2 = l2.value
        if(remainder == 1):
            newVal = val1 + val2 + remainder
            remainder = 0
        else:
            newVal = val1 + val2
        
        #Add one to remainder if digit value exceeds 9
        if(newVal > 9):
            remainder = 1
            newVal = newVal - 10
        
        #Store new node in the return list
        if firstNode is True:
            currNode = linkedlistNode(newVal)
            prevNode = currNode
            result = prevNode
            firstNode = False
        else:
            currNode = linkedlistNode(newVal)
            prevNode.nextNode = currNode
            prevNode = prevNode.nextNode
        
        #Check if there are any values left in either provided list
        if l1.nextNode is None:
            break
        if l2.nextNode is None:
            break
        
        #Grab the next node from provided lists
        l1 = l1.nextNode
        l2 = l2.nextNode
    
    #Run if there are still remaining values in first list
    if l1.nextNode is not None:
        l1 = l1.nextNode
        while True:
            #Add next digits
            val1 = l1.value
            if(remainder == 1):
                val1 = val1 + remainder
                remainder = 0
            
            #Add one to remainder if digit value exceeds 9
            if(val1 > 9):
                remainder = 1
                val1 = val1 - 10
                
            #Store new node in the return list
            currNode = linkedlistNode(val1)
            prevNode.nextNode = currNode
            prevNode = prevNode.nextNode
            
            #Check if there are any values left in either provided list
            if l1.nextNode is None:
                break
            
            #Grab the next node from provided lists
            l1 = l1.nextNode
    
    #Run if there are still remaining values in second list
    if l2.nextNode is not None:
        l2 = l2.nextNode
        while True:
            #Add next digits
            val2 = l2.value
            if(remainder == 1):
                val2 = val2 + remainder
                remainder = 0
            
            #Add one to remainder if digit value exceeds 9
            if(val2 > 9):
                remainder = 1
                val2 = val2 - 10
                
            #Store new node in the return list
            currNode = linkedlistNode(val2)
            prevNode.nextNode = currNode
            prevNode = prevNode.nextNode
            
            #Check if there are any values left in either provided list
            if l2.nextNode is None:
                break
            
            #Grab the next node from provided lists
            l2 = l2.nextNode
    
    #If there is still a remainder left over
    if(remainder == 1):
        currNode = linkedlistNode(remainder)
        prevNode.nextNode = currNode
        prevNode = prevNode.nextNode
    
    return result
    
print("Hello World")
node1 = linkedlistNode(3)
node2 = linkedlistNode(7)
node3 = linkedlistNode(5)

node1.nextNode = node2
node2.nextNode = node3
list1 = node1

node4 = linkedlistNode(5)
node5 = linkedlistNode(8)
node6 = linkedlistNode(0)
node7 = linkedlistNode(9)

node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
list2 = node4

combine = add_two_numbers(list1, list2)

while True:
    print (combine.value)
    if combine.nextNode is None:
        print ("End")
        break
    combine = combine.nextNode