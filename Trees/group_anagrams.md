# Group Anagrams

## Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Two strings are anagrams if they contain the same characters with the same frequency.

---

## Example

Input:
["eat","tea","tan","ate","nat","bat"]

Output:
[["eat","tea","ate"],["tan","nat"],["bat"]]

Explanation:
Words that contain the same characters belong to the same group.

---

## Approach

1. Use a HashMap (dictionary) to group words.
2. For each word:
   - Sort the characters of the word.
   - Use the sorted word as the key.
3. Append the original word to the list corresponding to that key.
4. Return all grouped values.

Example:

eat → sorted → aet  
tea → sorted → aet  
ate → sorted → aet  

All share the same key, so they belong to the same group.
