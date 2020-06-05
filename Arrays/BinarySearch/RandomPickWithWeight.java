// June Challenge Day 5: RandomPickWithWeight
// Problem:
// Given an array w of positive integers, where w[i] describes the weight of 
// index i, write a function pickIndex which randomly picks an index in 
// proportion to its weight.

// Note:
// 1 <= w.length <= 10000
// 1 <= w[i] <= 10^5
// pickIndex will be called at most 10000 times.

// Example 1:
// Input: 
// ["Solution","pickIndex"]
// [[[1]],[]]
// Output: [null,0]

// Example 2:
// Input: 
// ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
// [[[1,3]],[],[],[],[],[]]
// Output: [null,0,1,1,1,0]

// Explanation of Input Syntax:
// The input is two lists: the subroutines called and their arguments. 
// Solution's constructor has one argument, the array w. pickIndex has no 
// arguments. Arguments are always wrapped with a list, even if there aren't any.

// ============================================================================
// Personal Notes:
// Question is confusing, but it's asking to create a weighted random
// number generator. The input gives the weight at each index.
// Output always begins with null and then gives the number generated each time
// pickNumber() is called.

// For Example 1 since there is only [1], it means index 0 has a weight of 100%

// For Example 2 there is a total weight of (1 + 3) = 4, meaning that
// index 0 has a weight of 1/4 and index 1 has a weight of 3/4.

// Key takeaway from problem: Arrays.binarySearch(array, searchKey) will return
// index of searchKey if found, but more interestingly: 
// it will otherwise, returns (-(insertion point) – 1). The insertion point is 
// defined as the point at which the key would be inserted into the array: the 
// index of the first element greater than the key, or a.length if all elements 
// in the array are less than the specified key. 
// ============================================================================

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */

class Solution {
    
    int totalWeight = 0;
    int[] weightedArray;
    Random rand = new Random();
    
    public Solution(int[] w) {
        // Iterate through array w while creating a weighted array.
        // Weighted array accounts for the weight of each index
        // by making the element at that index the running total.
        // Generate a random integer and use weighted array
        // to determine which number would be generated had 
        // weights been assigned during generation
        // (do this by checking if integer > running total of index)
        
        // runtime: O(n): iterate through all n indices for total
        //                binary search: logn as values are ascending
        // space: O(n): weightedArray size equal to that of w
        
        // use a weighted array that pickIndex() can reference
        weightedArray = new int[w.length];
        
        for (int i = 0; i < w.length; i++) {
            // keep track of total weight of w
            totalWeight += w[i];
            
            // subtract 1 to account for java's random number generator
            // as it is [0, n) with 0 inclusive and n exclusive
            weightedArray[i] = totalWeight - 1;
        }
    }
    
    public int pickIndex() {
        // generate integer [0, totalWeight)
        int randInt = rand.nextInt(totalWeight);
        
        // if index of search key is contained in the array
        // Arrays.binarySearch returns index of the search key 
        int ans = Arrays.binarySearch(weightedArray, randInt);
        
        // otherwise, returns (-(insertion point) – 1). 
        // The insertion point is defined as the point at which 
        // the key would be inserted into the array: the index 
        // of the first element greater than the key, or a.length
        // if all elements in the array are less than the specified key. 
        if (ans < 0) {
            ans = -ans - 1;
        }
        
        return ans;
    }
}