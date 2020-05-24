# 905. Sort Arary by Parity
# Difficulty: Easy
# Problem:
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
# followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# runtime: O(n): iterate through all elements to check if even or odd
# space: O(1): creates two pointers to sort in place
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # two pointer solution
        # have one pointer at beginning of array, one at end
        # if pointer at beginning encounters an even number, increment it
        # if pointer at end encounters an odd number, decrement it
        # if pointer at beginning encounters odd number, swap with pointer at end
        
        # once pointers cross, we have fully sorted
        while (left < right): 
            # while left is an even number and not out of bounds, increment
            while (A[left] % 2 == 0 and left < len(A) - 1): 
                left += 1
            # while right is an odd number and not out of bounds, decrement
            while (A[right] % 2 == 1 and right > 0):
                right -= 1
            # swap only if left is odd, right is even, and pointers have not crossed
            if (A[left] % 2 == 1 and A[right] % 2 == 0 and left < right):
                A[left], A[right] = A[right], A[left]
        
        return A