"""
LeetCode 349 - Intersection of Two Arrays
Difficulty: Easy
Topic: Arrays, Hash Set

Problem Link:
https://leetcode.com/problems/intersection-of-two-arrays/

Approach:
Brute force comparison using nested loops.

Time Complexity: O(n * m)
Space Complexity: O(n)
"""

class Solution:
    def intersection(self, nums1, nums2):
        result = set()

        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)

        return list(result)
