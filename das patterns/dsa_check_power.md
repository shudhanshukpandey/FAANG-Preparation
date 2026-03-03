Given two positive numbers x and y, check if y is a power of x or not.
Examples : 

Input:  x = 10, y = 1
Output: True
x^0 = 1

Input:  x = 10, y = 1000
Output: True
x^3 = 1

Input:  x = 10, y = 1001
Output: False


This approach efficiently checks if a number y is a power of another number x by leveraging exponential growth and binary search. It first attempts to reach or exceed y by repeatedly squaring x, which significantly reduces the number of multiplications compared to simple iteration. If the squared value matches y, the function returns true. If it overshoots y, a binary search is performed between the last two computed powers of x to find an exact match.


import math

def isPower(x, y):
    if x == 1:
        return y == 1
    
    if y == 1:
        return 1
    pow = x

    while pow < y:
        pow *= x

    if pow == y:
        return True

    low, high = x, pow
    while low <= high:
        mid = low + (high - low) // 2
        result = int(x ** int(math.log(mid) / math.log(x)))

        if result == y:
            return True
        if result < y:
            low = mid + 1
        else:
            high = mid - 1

    return False

print("true" if isPower(10, 1) else "false")
print("true" if isPower(1, 20) else "false")
print("true" if isPower(2, 128) else "false")
print("true" if isPower(2, 30) else "false")




import math

def isPower(x, y):
    res1 = math.log(y) / math.log(x)
    return res1 == math.floor(res1)

print(isPower(2, 128))