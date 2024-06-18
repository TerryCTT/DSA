// 49. Group Anagrams
// NeetCode: Arrays & Hashing 4/9
// Solved on 6/17/24
// Difficulty: Medium
// Problem:

// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Example 2:
// Input: strs = [""]
// Output: [[""]]

// Example 3:
// Input: strs = ["a"]
// Output: [["a"]]
 

// Constraints:

// 1 <= strs.length <= 10^4
// 0 <= strs[i].length <= 100
// strs[i] consists of lowercase English letters.

// Topics: Arrays, HashTable, String, Sorting

// =====================================================================================

// Intuition:
// Anagrams will have the same form once they are sorted. We can sort each string within the array and group
// identical strings. 


class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Approach:
        // (1) Create a hashmap to help group our anagrams
        // (2) Iterate through list of strings and sort each string's letters to determine which strings are grouped together 
        //    (a) Words that are anagrams will have the same appearance in order of letters once they're sorted
        //    (b) We keep track of our anagrams and group them together by using our hashmap
        //       (i) Key: sorted string, Value: List of original unsorted strings that share this sorted value
        //       (ii) Check if current sorted string exists in hashmap, if it doesn't: create list and add current unsorted string
        //       (iii) if it does: append current list with current unsorted string at that sorted string's value
        // (3) Return list of grouped anagrams

        // time complexity: O(n * mlogm + k). 
        //   n is the number of strings in our list
        //   m is the number of characters in longest string
        //   k is number of different anagrams (# of different sorted strings)
        //   mlogm is the time it takes to sort characters in longest string in our list, and each string is sorted separately
        //   k is the number of different anagrams in our hashtable that we iterate through to turn into a list
        // space complexity: O(n). Our list of list of strings is dependent on number of strings given as input, and same with hashmap.

        Map<String, List<String>> sortedStrs = new HashMap<>(); // (1)

        for (String word : strs) { // (2)

            char chars[] = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);

            if (!map.containsKey(sortedWord)) { // (ii)
                map.put(sortedWord, new ArrayList<>());
            }
            
            map.get(sortedWord).add(word); // (iii)

        }

        return new ArrayList<>(map.values()); // (3)
        // Still works in cases of no given strings or 1 given string

    }
}