Given two positive integers a and b. Find the Least Common Multiple (LCM) of a and b.
LCM of two numbers is the smallest number which can be divided by both numbers. 


This approach to calculating the Least Common Multiple (LCM) involves starting from the greater of the two numbers and checking if it's divisible by the smaller number. It iterates through multiples of the larger number, incrementing by the larger number itself in each step. The first multiple that is divisible by the smaller number is the LCM. This method is simple and intuitive, but it can be inefficient, especially for large numbers, as it checks multiple values until a match is found.

def lcm(a, b):
    
    # Larger value
    g = max(a, b) 
    
    # Smaller value
    s = min(a, b)  

    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 

if __name__ == '__main__':
    a = 10
    b = 5
    print(lcm(a, b))


An efficient solution is based on the below formula for LCM of two numbers 'a' and 'b'. 

# function for gcd
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

if __name__ == '__main__':
    a = 10
    b = 5
    print(lcm(a, b))