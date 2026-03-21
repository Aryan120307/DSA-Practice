"""
LeetCode 217 - Contains Duplicate
Difficulty: Easy
Topic: Arrays, Hash Set

Problem Link:
https://leetcode.com/problems/contains-duplicate/

Approach:
Use a hash set to track seen elements.
If an element is already in the set, return True.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
