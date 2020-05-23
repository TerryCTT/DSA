# 961. N-Repeated Element in Size 2N Array
# Difficulty: Easy
# Problem:
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

# Return the element repeated N times.

# Example 1:
# Input: [1,2,3,3]
# Output: 3

# Example 2:
# Input: [2,1,2,5,3,2]
# Output: 2

# Example 3:
# Input: [5,1,5,2,5,3,5,4]
# Output: 5

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Create a dictionary
        # interate through elements of array, checking if it exists in dictionary
        # if exists, return that element since only one duplicate number in array
        # otherwise, store into dictionary
        numsSeen = dict()
        
        for num in A:
            if (numsSeen.get(num) == 1):
                return num
            else:
                numsSeen[num] = 1
        
        # impossible for value to not have been found if correct input array
        # but return -1 if no duplicate is found
        return -1;