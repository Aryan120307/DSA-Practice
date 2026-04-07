"""
LeetCode 75 - Sort Colors
Difficulty: Medium
Topic: Arrays, Two Pointers

Problem Link:
https://leetcode.com/problems/sort-colors/

Approach:
Dutch National Flag Algorithm (3-way partitioning)

We maintain three pointers:
- low → boundary for 0s
- mid → current element
- high → boundary for 2s

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
