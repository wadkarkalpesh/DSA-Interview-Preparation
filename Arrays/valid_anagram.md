# Valid Anagram

Topic: Hashing / Frequency Count

## Approach
If the string lengths differ, they cannot be anagrams.

Count the frequency of each character in both strings using dictionaries.
Compare the counts. If every character frequency matches, return True.

## Time Complexity
O(n)

## Space Complexity
O(26) ≈ O(1)
(only lowercase English letters)
