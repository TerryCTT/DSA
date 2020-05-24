// 1380. Lucky Numbers in a Matrix
// Difficulty: Easy
// Problem:
// Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

// A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

// Example 1:
// Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
// Output: [15]
// Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

// Example 2:
// Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
// Output: [12]
// Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

// Example 3:
// Input: matrix = [[7,8],[1,2]]
// Output: [7]


// runtime: O(2*m*n): iterate through all elements to find mins and maxes
//                    iterate again to check if lucky
// space: O(m + n) m size array to hold mins, n size array to hold maxes

import java.util.*;

class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        // create 2 arrays: 
        // first to hold min of each row
        // second to hold max of each column
        // iterate through matrix once to populate arrays
        // iterate through again to check if numbers are lucky
        
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[] minRows = new int[rows];
        int[] maxCols = new int[cols];
        List<Integer> luckyNums = new ArrayList<Integer>();
        
        // set default min and max values for our arrays
        Arrays.fill(minRows, Integer.MAX_VALUE);
        Arrays.fill(maxCols, Integer.MIN_VALUE);
        
        
        // iterate through matrix to find mins of each row and maxes of each col
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] < minRows[i]) {
                    minRows[i] = matrix[i][j];
                }
                if (matrix[i][j] > maxCols[j]) {
                    maxCols[j] = matrix[i][j];
                }
            }
        }
        
        // iterate through each element to check if lucky
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == minRows[i] && matrix[i][j] == maxCols[j]) {
                    luckyNums.add(matrix[i][j]); 
                }
            }
        }
        
        return luckyNums;
    }
}