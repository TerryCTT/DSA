// 728. Self Dividing Numbers
// Difficulty: Easy
// Problem:
// A self-dividing number is a number that is divisible by every digit it contains.

// For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

// Also, a self-dividing number is not allowed to contain the digit zero.

// Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

// Example 1:
// Input: 
// left = 1, right = 22
// Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]



// runtime: O(n*k) where n is the amount of numbers between left and right
//                 and k is the length of right
// space: O(n) where n is the number of digits that self divide (at most n)
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        // 1. iterate through numbers starting with left and ending with right
        // 2. iterate through digits of our number
        //  a. if digit is zero, move on to next number
        //  b. if digit does not divide our number, move on to next number
        //  c. if conditions a and b are not met, every digit divides number
        //     and we add number to list
        
        List<Integer> selfDividers = new ArrayList<Integer>();
        int lastDigit;
       
        // 1. iterate through numbers starting with left and ending with right
        for (int i = left; i <= right; i++) {
            // 2. iterate through digits of our number
            boolean selfDivides = true;
            int otherDigits = i;
                
            while (otherDigits != 0) {
                lastDigit = otherDigits % 10;
                otherDigits = otherDigits / 10;
                // a. if digit is zero, move on to next number
                // b. if digit does not divide our number, move on to next number
                if (lastDigit == 0 || i % lastDigit != 0) {
                    selfDivides = false;
                    break;
                }
            }
            // every digit divides number and we add number to list
            if (selfDivides) {
                selfDividers.add(i);
            }
        }
        return selfDividers;
    }
}