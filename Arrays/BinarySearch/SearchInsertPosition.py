# June Challenge Day 10: Search Insert Position
# Problem:
# Given a sorted array and a target value, return the index if the target 
# is found. If not, return the index where it would be if it were inserted 
# in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # We implement binary search
        # Note that Java's Arrays.binarySearch(arr, target) does exactly
        # what the problem statement asks

        # runtime: O(logn): cut values we search through in "half" each time
        # space: O(1): constant space using pointers left, right, mid

        left = 0
        right = len(nums) - 1
        
        
        while (left <= right):
            mid = left + (right - left) // 2
            
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                # target is in lower half
                right = mid - 1
            else:
                # target is in upper half
                left = mid + 1
        
        # left is where the insertion position would be
        return left