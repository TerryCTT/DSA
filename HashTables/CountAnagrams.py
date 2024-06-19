# 2514. Count Anagrams
# Solved on 6/18/24
# Difficulty: Hard
# Problem:

# You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

# A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

# For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.

# Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 10^9 + 7.

 
# Example 1:
# Input: s = "too hot"
# Output: 18
# Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".

# Example 2:
# Input: s = "aa"
# Output: 1
# Explanation: There is only one anagram possible for the given string.

# Constraints:

# 1 <= s.length <= 10^5
# s consists of lowercase English letters and spaces ' '.
# There is single space between consecutive words.

# Topics: 

# =====================================================================================

# Intuition:
# The question calls for us to "return the number of distinct anagrams of s", which essentially means to calculate the number
# of permutations of s. 
# To calculate # permutations of n items where p items are identical, q items are identical, 
# r items are identical, etc., we use the formula given by: 
# # permutations = (n!) / ( (p!)(q!)(r!) ) 
# In the context of our problem: 
# n is number of letters in each section (section being the letters between spaces) of string
# p, q, r, etc are numbers of each identical letters in each section of string
# We take the product of each of these permutations to calculate number of distinct anagrams of s
#
# To verify this using example 1 from above, # permutations for s = "too hot": ( (3!) / (2!) ) * (3!)! = 3 * 6 = 18  

class Solution:
    def countAnagrams(self, s: str) -> int:
        # Approach:
        # (1) Create variable to store number of permutations
        # (2) Iterate through each word within string and calculate permutations
        #     (a) Calculate total number of characters in each word and numbers of each identical letter
        #     (b) Use permutation formula detailed above
        #     (c) Update permutation count with product of each word's number of permutations
        # (3) Return total number of distinct permutations

        strPermutations = 1 # (1)

        words = s.split()

        for word in words: # (2)
            numLetters = len(word)
            letterCounts = {}

            for letter in word: # (3)
                if letter in letterCounts:
                    letterCounts[letter] += 1
                else:
                    letterCounts[letter] = 1 

            wordPermutations = math.factorial(numLetters) # (b)

            for key in letterCounts:
                wordPermutations //= math.factorial(letterCounts[key]) # (b)

            strPermutations *= wordPermutations # (c)

        return int(strPermutations) % (10**9 + 7) # (3)