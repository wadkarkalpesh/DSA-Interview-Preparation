# Search in Rotated Sorted Array

Topic: Modified Binary Search

## Approach
At each step determine which half is sorted.
Check if target lies in that half and discard the other half.

## Time Complexity
O(log n)

## Space Complexity
O(1)