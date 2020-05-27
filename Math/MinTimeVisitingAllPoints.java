// 1266. Minimum Time Visiting All Points
// Difficulty: Easy
// Problem:
// On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
// Your task is to find the minimum time in seconds to visit all points.

// You can move according to the next rules:

// In one second always you can either move vertically, horizontally by one unit or diagonally
// (it means to move one unit vertically and one unit horizontally in one second).
// You have to visit the points in the same order as they appear in the array.

// Example 1:
// Input: points = [[1,1],[3,4],[-1,0]]
// Output: 7
// Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
// Time from [1,1] to [3,4] = 3 seconds 
// Time from [3,4] to [-1,0] = 4 seconds
// Total time = 7 seconds

// Example 2:

// Input: points = [[3,2],[-2,2]]
// Output: 5

// runtime: O(n): n is the number of points 
// space: O(1): constant space, use minTime counter

class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        // the minimum time between two points is equal to the absolute value of 
        // the greater difference between their X and Y values
        
        // edge cases for empty arrays or not enough points to calculate distance
        if (points.length < 1 || points == null) {
            return 0;
        } 
        
        int minTime = 0;
        
        // start at 1 to prevent out of bounds errors
        // move from point i-1 to point i
        for (int i = 1; i < points.length; i++) {
            // calculate X difference
            int xDifference = points[i][0] - points[i-1][0];
            // calculate Y difference
            int yDifference = points[i][1] - points[i-1][1];
            
            // add the greater of the absolute value of differences
            minTime+= Math.max(Math.abs(xDifference), Math.abs(yDifference));
        }
        return minTime;
    }
}