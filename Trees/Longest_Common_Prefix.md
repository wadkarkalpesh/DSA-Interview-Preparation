# Longest Common Prefix

## Problem
Given an array of strings `strs`, return the longest common prefix among all strings.

If there is no common prefix, return an empty string `""`.

### Example

Input:
["flower","flow","flight"]

Output:
"fl"

Explanation:
The longest prefix shared by all strings is "fl".

---

## Approach

1. Assume the first string is the prefix.
2. Compare the prefix with the next string.
3. If the prefix does not match the beginning of the word, remove the last character.
4. Continue until the prefix matches.
5. Repeat this process for all words.

---