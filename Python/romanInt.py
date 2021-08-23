#Roman to Integer

#There are 3 conditions that must be satisfied in order to return a result

#1. Length must be between 1 and 15
def check_length(s):
    check = len(s)
    if (check >= 1 and check <= 15):
        return True
    else:
        return False

#2. All characters must be valid roman letters
def check_char(s):
    check = s
    roman_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    matched_list = [characters in roman_letters for characters in check]
    result = all(matched_list)
    return result

#3. The value returned must be betwen 1 and 3999
def check_val(i):
    check = i
    if(check > 0 and check < 4000):
        return True
    else:
        return False

#Converts roman value or special value into integers
def roman_to_int(s):
    num = 0
    if(s == "I"):
        num = 1
    if(s == "V"):
        num = 5
    if(s == "X"):
        num = 10
    if(s == "L"):
        num = 50
    if(s == "C"):
        num = 100
    if(s == "D"):
        num = 500
    if(s == "M"):
        num = 1000
    
    return num

#Start of roman to int converter
def converter(roman):
    r = roman
    curr = "Z"
    sec = "Z"
    combine = "ZZ"
    temp = 0
    result = 0
    i = 0
    
    #Conditions that must be true in order to proceed
    #Note: The 3rd condition is checked when the number is converted
    length = check_length(r)
    characters = check_char(r)
    
    if length is True and characters is True:
        #Go through the list of roman letters
        while (i < len(r)):
            curr = r[i]
            
            #Condition checks if there is a number after to check for special value
            if ((i + 1) < len(r)):
                sec = r[i + 1]
                
                #Used if it is a special value
                if roman_to_int(sec) > roman_to_int(curr):
                    temp = roman_to_int(sec) - roman_to_int(curr)
                    result += temp
                    i += 2
                #Used if not special value
                else:
                    temp = roman_to_int(curr)
                    result += temp
                    i += 1
            #Used for last element in the list
            else:
                temp = roman_to_int(curr)
                result += temp
                i += 1
                
        #Final check
        value = check_val(result)
        if value is True:
            print(result)
        else:
            if result < 1:
                print("ERROR: Value is lower than 1.")
            elif result > 3999:
                print("ERROR: Value exceeds 3999.")
            else:
                print("ERROR!")
    else:
        if length is False:
            print("Invalid Length!")
        if characters is False:
            print("Invalid Characters!")

test1 = "III"
test2 = "IV"
test3 = "IX"
test4 = "LVIII"
test5 = "MCMXCIV"
test6 = "ABBBBBBBBBBBBBBBBBBBBBBB"

converter(test1)
converter(test2)
converter(test3)
converter(test4)
converter(test5)