# June Challenge Day 9: Is Subsequence
# Problem:
# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original 
# string by deleting some (can be none) of the characters without disturbing 
# the relative positions of the remaining characters. (ie, "ace" is a 
# subsequence of "abcde" while "aec" is not).

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and 
# you want to check one by one to see if T has its subsequence. In this 
# scenario, how would you change your code? 

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
 
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate through chars of s by comparing with chars of t.
        # if s and t match, we move onto next char in s and t.
        # if s and t do not match, we move onto only next char in t.
        # if all char in s are found, we have subsequence and return true.
        # otherwise we do not have a subsequence if t finishes processing
        # without fully processing s and return false.
        
        # runtime: O(n): where n is the number of char in t
        # space: O(1): constant space, 2 pointers to iterate through s and t
        
        # edge cases
        if (len(s) == 0):
            return True
        
        if (len(t) == 0):
            return False
        
        sIndex = 0
        tIndex = 0
        
        # process chars in s and t to look for matches
        # we finish either when all chars in s are processed
        # or when all chars in t are processed
        while (sIndex < len(s) and tIndex < len(t)):
            # proceed to next char in s only if a match is found
            if (s[sIndex] == t[tIndex]):
                sIndex += 1
            # proceed to next char in t after every check
            tIndex += 1
        
        # s is a subsequence of t only if all char in s were processed,
        # meaning we found a match for each char in s
        return sIndex == len(s)