# 2460. Apply Operations to an Array
# LeetCode Daily: 3/1/25
# Difficulty: Easy
# Problem:

# You are given a 0-indexed array nums of size n consisting of non-negative integers.
 
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.

# After performing all the operations, shift all the 0's to the end of the array.

# For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

# Return the resulting array.

# Note that the operations are applied sequentially, not all at once.

# Example 1:
# Input: nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]
# Explanation: We do the following operations:
# - i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
# - i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
# - i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
# - i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
# - i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
# After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].

# Example 2:
# Input: nums = [0,1]
# Output: [1,0]
# Explanation: No operation can be applied, we just shift the 0 to the end.


# Intuition:
# The conditions and operations for our if - else statement are given in the description
# We iterate through the array once to perform those operations
# We iterate through the array a second time to shift the 0's
# To do this, we use two pointers:
# - First pointer: starts at the front of the array and looks for any 0's to move
# - Second pointer: starts at the end of the array and keeps track of where 0's are moved to
#                   each time a zero is moved to the back, we decrement the end pointer
# We are done iterating once the front and end pointers cross

# Complexities:
# time: O(n), we iterate through all of array once o(n) for operations and then once again for shifting 0's: o(n) + o(n) = o(2n) = O(n)
# space: O(1), we use two pointers to keep track of positions when shifting 0's
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        
        front = 0
        end = len(nums)

        while front < end:
            if nums[front] == 0:
                nums.insert(end, 0)
                end = end - 1
                del nums[front]
            else:
                front += 1
                # we only increment here because above if we delete the
                # element at index front and increment, we'd skip an element

        return nums


