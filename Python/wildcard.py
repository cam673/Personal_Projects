#Wildcard Matching

#Given a string, find out if the pattern matches the string
#Note: Two special characters may be in these patterns, they have the following properties
#? - Can be any single character
#* - Can be any pattern(collection of characters) including an empty string

def wildcard_match(s, p):
    string = s
    pattern = p
    matches = True
    
    #Check if the strings match
    i = 0
    j = 0
    while i < len(string):
        #return false if it fails the following checks
        #if the characters don't match
        if string[i] != pattern[j]:
            if pattern[j] == '*':
                if bool(pattern[j+1]):
                    print("check")
                else:
                    return matches
            #before marking as false check if it is a ?
            if pattern[j] != '?':
                matches = False
                return matches
        #end of the list string but not pattern
        if (len(string) - i) == 1 and (len(pattern) - j) != 1:
            print("End of string list.")
            print("Items in pattern list remain.")
            matches = False
            return matches
        #end of the list pattern but not string
        if (len(pattern) - j) == 1 and (len(string) - i) != 1:
            print("End of pattern list.")
            print("Items in string list remain.")
            matches = False
            return matches
        i += 1
        j += 1
    
    #if all conditions are satisfied
    return matches

s1 = "abbda"
p1 = "*a"
s2 = "gsooi"
p2 = "gs?oi"
s3 = "pi"
p3 = "pie"
s4 = "woof"
p4 = "*woof"

r2 = wildcard_match(s2, p2)
print(r2)
r3 = wildcard_match(s3, p3)
print(r3)