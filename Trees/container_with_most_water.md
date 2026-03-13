# Container With Most Water

## Problem
You are given an integer array `height` where each element represents the height of a vertical line.

Find two lines that together with the x-axis form a container that holds the **maximum amount of water**.

Return the maximum amount of water the container can store.

---

## Example

Input:
[1,8,6,2,5,4,8,3,7]

Output:
49

Explanation:
The maximum water is obtained between the lines with heights 8 and 7.

---

## Approach (Two Pointer Technique)

1. Use two pointers:
   - `left` starting at the beginning
   - `right` starting at the end

2. Calculate the area using:

   area = min(height[left], height[right]) × (right - left)

3. Update the maximum area.

4. Move the pointer with the **smaller height** because the height of the container is limited by the shorter line.

5. Continue until `left` meets `right`.
