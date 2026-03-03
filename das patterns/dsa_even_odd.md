We can check the remainder when divided by 2. If the remainder is 0, the number is even, otherwise it is odd.

def isEven(n):
    # finding remainder of n
    rem = n % 2; 
    if rem == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")


The last bit of all odd numbers is always 1, while for even numbers it’s 0. So, when performing bitwise AND operation with 1, odd numbers give 1, and even numbers give 0.

Examples:

15  ->               1 1 1 1
                    &  0 0 0 1
                       -------
                       0 0 0 1 , so this we can say it is an odd number.

44 ->        1 0 1 1 0 0
            &  0 0 0 0 0 1
                 ----------
                0 0 0 0 0 0 , so this we can say it is an even number.


def isEven(n):
    # taking bitwise and of n with 1 
    if (n & 1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")