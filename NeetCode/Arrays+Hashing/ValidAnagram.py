# 242. Valid Anagram
# NeetCode: Arrays & Hashing 2/9
# Solved on 6/12/24
# Difficulty: Easy
# Problem:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# Answer: adjust array to include Unicode characters.

# Topics: Hashtable, String, Sorting

# =====================================================================================

# solution using python's Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# solution without using python's Counter

# Intuition:
# We can solve iterating through each character in first string s and adding to an array that represents the totals of each letter we encounter in string s . 
# We then iterate through each character in second string t and check to see if the character exists in the array we created for string s. 
# If the character does not exist, then s and t are not anagrams. If the character does exist, we decrement the count. If the count falls 
# below zero, s and t are not anagrams. After iterating through all characters of t, we check that all values in array are equal to zero. 
# If they are, then we know s and t are anagrams.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach:
        # (1) Set up an array that represents the totals of each letter we encounter in strings s.
        #    (a) Since our constraints are that s and t consist of only lowercase English letters, the array is of size 26
        #    (b) first index 0 representing a, index 1 representing b, ... , index 25 representing z
        # (2) Iterate through letters of s, incrementing the counts of each letter in the array whenever we encounter them.
        # (3) Iterate through letters of t, decerementing the counts of each letter in the array whenever we encounter them.
        #    (a) If any of the counts ever fall below zero, s and t are not anagrams and we return False
        # (4) Once each string has been iterated through, we check that each value in the array is zero. 
        #    (a) If all values are zero, s and t are anagrams and we return True. 
        #    (b) If any value is not zero, s and t are not anagrams and we return False.
    

        # time complexity: O(n). Worst case: s and t are anagrams or differ in count for last character in array.
        # space complexity: O(1). store counts of letters in s and t in one array of size 26. 

        # if s and t are different lengths, they cannot be anagrams
        if (len(s) != len(t)) : return False

        # (1)
        letterCount = [0] * 26

        # (2)
        for letter in s:
            letterCount[letter - 'a'] += 1

        # (3)
        for letter in t:
            letterCount[letter - 'a'] -= 1
            if letterCount[letter - 'a'] < 0: return False

        # (4)
        for count in letterCount:
            if letterCount != 0: return False

        return True