# 1380. Lucky Numbers in a Matrix
# Difficulty: Easy
# Problem:
# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

# Example 2:
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:
# Input: matrix = [[7,8],[1,2]]
# Output: [7]

# runtime: O(m*n): iterate through all elements to find mins and maxes
# space: O(m+n): set of m mins and n maxes

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # use set comprehension to create set of min row values
        # use set comprehension and zip on unpacked *matrix 
        # to create set of max col values
        
        # since all elements in matrix are distinct, intersection of the two sets
        # are guaranteed to be of same row/col 
        
        luckyNums = list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})
        
        return luckyNums;