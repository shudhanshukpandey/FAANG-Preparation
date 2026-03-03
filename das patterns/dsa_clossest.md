Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

Examples: 

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.


We first compute the quotient q = n / m, then calculate two candidates:

n1 = m * q
 This is the closest multiple of m that is less than or equal to n.
n2 = m * (q + 1) or m * (q - 1)
 We choose q + 1 or q - 1 based on the signs of n and m:
If n and m have the same sign, use n2 = m * (q + 1)
 This moves in the direction toward n, getting the next closest multiple above n.
If n and m have opposite signs, use n2 = m * (q - 1)
 This accounts for the fact that increasing q would move away from n due to the sign flip, so we instead go backward to get the next closest multiple.
Then we return the one (n1 or n2) that has the smaller absolute difference from n.

If both have the same distance from n, return the one with the greater absolute value, as required.


def closestNumber(n, m) :
    q = int(n / m)
    
    # 1st possible closest number
    n1 = m * q
    
    # 2nd possible closest number
    if((n * m) > 0) :
        n2 = (m * (q + 1)) 
    else :
        n2 = (m * (q - 1))
    
    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)) :
        return n1
    
    # else n2 is the required closest number 
    return n2
    
    
if __name__ == "__main__":
  n = 13; m = 4
  print(closestNumber(n, m))