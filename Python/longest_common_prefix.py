#Longest Common Prefix

#Check to see what the longest prefix within an array of words is
def longestPrefix(words):
    result = ""
    prefix = ""
    accum = 0
    base = words[0] #Selected word to grab prefixes from
    
    #pick a word from the list and grab all possible prefixes from it
    #Note: you do not have to do the same for each word since the prefix has to be true for all words
    i = 0
    while i < len(base):
        j = i
        prefix = ""
        
        while j < len(base):
            #generate new prefix
            prefix = prefix + base[j]
            
            #check which words contain the prefix
            for t in words:
                if prefix in t:
                    accum += 1
            
            #if all words contain the prefix, add word to result if the current prefix is bigger than result
            if accum == len(words):
                if len(prefix) > len(result):
                    result = prefix
            
            accum = 0
            j += 1
        i += 1
    
    return result

example1 = ["fleece", "flap", "floor"]
example2 = ["dog", "sock", "wrench"]

res1 = longestPrefix(example1)
print(res1)