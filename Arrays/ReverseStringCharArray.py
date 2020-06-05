# June Challenge Day 4: Reverse String
# Problem:
# Write a function that reverses a string. The input string is given 
# as an array of characters char[].

# Do not allocate extra space for another array, you must do this by 
# modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # iterate through array using two pointers
        # one pointer starts at head of array, other pointer starts at end
        # swap values at each pointer until reaching halfway point of array
        
        # runtime: O(n): iterate through half of array s
        # space: O(1): constant space with 2 pointers and 1 temp var
        
        if (len(s) <= 1 or s is None):
            return
        
        head = 0
        tail = len(s) - 1
        
        while (head < tail):
            temp = s[head]
            s[head] = s[tail]
            s[tail] = temp
            
            head += 1
            tail -= 1