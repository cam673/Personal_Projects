#ZigZag Reader

#Read a line in a zigzag format using the provided row size

def zigzag_reader(message, rows):
    #set up rows
    row_num = [""] * rows
    reverse = False
    inc = 1
    pos = 0
    result = ""
    
    if rows == 1:
        print("Row length of 1 cannot be zigzagged.")
        return message
    
    #place string characters in the rows
    for i in message:
        #find out if going down or right-up
        if reverse is False:
            pos = inc - 1
            row_num[pos] = row_num[pos] + i
            inc += 1
        if reverse is True:
            pos = inc - 1
            row_num[pos] = row_num[pos] + i
            inc -= 1
        
        #Figure out if direction needs to be changed
        if inc == rows:
            reverse = True
        if inc == 1:
            reverse = False
    
    #merge rows into final result string
    j = 0
    while j < rows:
        result = result + row_num[j]
        j += 1
    
    return result

example1 = "PAYPALISHIRING"
row1 = 3
gen_res1 = zigzag_reader(example1, row1)
print(gen_res1)