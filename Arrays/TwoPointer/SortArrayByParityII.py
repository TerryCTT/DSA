# 922. Sort Array by Parity II
# Difficulty: Easy
# Problem: 
# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.

# Example 1:
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


# runtime: O(n): iterate through half of elements (odds) in array A
# space: O(1): two pointers and in place sorting
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # two pointer solution
        # have one pointer at beginning of array, one at end
        # if pointer at beginning encounters an even number, increment it
        # if pointer at end encounters an odd number, decrement it
        # if pointer at beginning encounters odd number, swap with pointer at end
        
        evenPtr = 0;
        # iterate through odd indices (starting at 1 and incrementing by 2)
        for i in range(1, len(A), 2):
            # if we find an even element, it's out of place
            if (A[i] % 2 == 0):
                # find the first odd element in an even place
                while (A[evenPtr] % 2 == 0):
                    evenPtr += 2
                # swap the even and odd elements out of place
                A[evenPtr], A[i] = A[i], A[evenPtr]
        return A