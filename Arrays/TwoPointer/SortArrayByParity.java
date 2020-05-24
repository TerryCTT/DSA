// 905. Sort Arary by Parity
// Difficulty: Easy
// Problem:
// Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
// followed by all the odd elements of A.

// You may return any answer array that satisfies this condition.

// Example 1:
// Input: [3,1,2,4]
// Output: [2,4,3,1]
// The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

// runtime: O(n): iterate through all elements to check if even or odd
// space: O(1): creates two pointers and a temp to sort in place
class Solution {
    public int[] sortArrayByParity(int[] A) {
        // two pointer solution
        // have one pointer at beginning of array, one at end
        // if pointer at beginning encounters an even number, increment it
        // if pointer at end encounters an odd number, decrement it
        // if pointer at beginning encounters odd number, swap with pointer at end
        
        int left = 0;
        int right = A.length - 1;
        int temp = 0;
        
        // once pointers cross, we have fully sorted
        while (left < right) {
            // while left is an even number and not out of bounds, increment
            while (A[left] % 2 == 0 && left < A.length - 1) {
                left++;
            }
            // while right is an odd number and not out of bounds, decrement
            while (A[right] % 2 == 1 && right > 0) {
                right--;
            }
            // swap only if left is odd, right is even, and pointers have not crossed
            if (A[left] % 2 == 1 && A[right] % 2 == 0 && left < right) {
                temp = A[left];
                A[left] = A[right];
                A[right] = temp;
            }
        }
        
        return A;
        
    }
}