"""
LeetCode 189 - Rotate Array
Difficulty: Medium
Topic: Arrays

Problem Link:
https://leetcode.com/problems/rotate-array/

Approach:
Use array slicing to rotate the array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        nums[:] = nums[-k:] + nums[:-k]
