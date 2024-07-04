# 49. Group Anagrams
# NeetCode: Arrays & Hashing 4/9
# Solved on 6/17/24
# Difficulty: Medium
# Problem:

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Topics: Array, HashTable, String, Sorting

# =====================================================================================

# More efficient solution with O(m*n)

# Intuition
# Anagrams will have the same number of letters. We can group each string within the array that have the same counts.

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        # Approach:
        # (1) Create a hashmap to help group our anagrams 
        # (2) Iterate through list of strings and count string's letters
        #    (a) Words that are anagrams will have the same letter counts
        #    (b) Create an array that will hold counts of letters for our strings
        #    (c) We keep track of our anagrams and group them together by using our hashmap
        #       (i) Key: array of letter counts, Value: List of original unsorted strings that share same letter counts
        #       (ii) Append current list at key with current unsorted string's letter count, at that letter count's value
        # (3) Return hashmap's values as list of grouped anagrams

        # time complexity: O(n * m). 
        #   n is the number of strings in our list
        #   m is the number of characters in longest string
        # space complexity: O(n). Our list of list of strings is dependent on number of strings given as input, and same with hashmap.

        letterCounts = defaultdict(list) # (1) default values will have empty list

        for word in strs: # (2)
            letters = [0] * 26 # (b)
            for letter in word:
               letters[ord(letter) - ord('a')] += 1
            letterCounts[tuple(letters)].append(word) # (ii) tuple since python does not allow list as key for hashmap

        return letterCounts.values() # (3)


# Original solution (less efficient) with O(n * mlogm + k) 

# Intuition:
# Anagrams will have the same form once they are sorted. We can sort each string within the array and group
# identical strings. 

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        # Approach:
        # (1) Create a hashmap to help group our anagrams
        # (2) Iterate through list of strings and sort each string's letters to determine which strings are grouped together 
        #    (a) Words that are anagrams will have the same appearance in order of letters once they're sorted
        #    (b) We keep track of our anagrams and group them together by using our hashmap
        #       (i) Key: sorted string, Value: List of original unsorted strings that share this sorted value
        #       (ii) Check if current sorted string exists in hashmap, if it doesn't: create list and add current unsorted string
        #       (iii) if it does: append current list with current unsorted string at that sorted string's value
        # (3) Return list of grouped anagrams

        # time complexity: O(n * mlogm + k). 
        #   n is the number of strings in our list
        #   m is the number of characters in longest string
        #   k is number of different anagrams (# of different sorted strings)
        #   mlogm is the time it takes to sort characters in longest string in our list, and each string is sorted separately
        #   k is the number of different anagrams in our hashtable that we iterate through to turn into a list
        # space complexity: O(n). Our list of list of strings is dependent on number of strings given as input, and same with hashmap.

        sortedStrs = {} # (1)

        for word in strs: # (2)
            sortedWord = ''.join(sorted(word))
            if sortedWord in sortedStrs:
                sortedStrs[sortedWord].append(word) # (iii)
            else:
                sortedStrs[sortedWord] = [word] # (ii)

        return list(sortedStrs.values()) # (3)
        # Still works in cases of no given strings or 1 given string


    
