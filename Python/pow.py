#Pow(x,n)

#Raise the value x by the power of n

#Power can be positive or negative
def Pow(x, n):
    result = 1
    
    if n == 0:
        return result
    
    i = 0
    if n > 0:
        while i < n:
            result = result * x
            i += 1
    else:
        while i > n:
            result = result / x
            i -= 1
    
    return result

x1 = 2
n1 = 10
n2 = -2
r1 = Pow(x1, n2)
print(r1)