# June Challenge Day 8: Power of Two
# Problem:
# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true 
# Explanation: 2^0 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: 218
# Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # repeatedly dividing n by 2 will reach either 1 or another odd number
        # in case of 1: n is a power of 2
        # in case of some other odd: n is not a power of 2
        
        # runtime: O(logn): we divide by 2 each time
        # space: O(1): store result in n each time
        
        # edge case
        if (n == 0): 
            return False
        
        # repeatedly dividing n by 2 will reach either 1 or another odd number
        while (n != 1 and n % 2 == 0):
            n /= 2
        
        # if we reach 1, n was a power of two
        if (n == 1):
            return True
        
        # any other odd means n was not a power of 2
        return False