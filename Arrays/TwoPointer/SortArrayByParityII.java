// 922. Sort Array by Parity II
// Difficulty: Easy
// Problem: 
// Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

// Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

// You may return any answer array that satisfies this condition.

// Example 1:
// Input: [4,2,5,7]
// Output: [4,5,2,7]
// Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


// runtime: O(n): iterate through half of elements (odds) in array A
// space: O(1): two pointers, a temp var, and in place sorting
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        // we know that exactly half the integers are even and half are odd
        // use a two pointer approach
        // first pointer will track even numbers stored at even indices starting at 0
        // second pointer will traverse array to check if A[i] is odd or even
        // if second pointer encounters an even element, swap element with first
        // pointer's element and increment even pointer by 2
        
        int evenPtr = 0;
        int temp;
        
        // iterate through odd indices (starting at 1 and incrementing by 2)
        for (int i = 1; i < A.length; i += 2) {
            // if we find an even element, it's out of place
            if (A[i] % 2 == 0) {
                // find the first odd element in an even place
                while (A[evenPtr] % 2 == 0) {
                    evenPtr += 2;
                }
                // swap the even and odd elements out of place
                temp = A[evenPtr];
                A[evenPtr] = A[i];
                A[i] = temp;
            }
        }
        return A;
    }
}