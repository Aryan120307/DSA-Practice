"""
LeetCode 350 - Intersection of Two Arrays II
Difficulty: Easy
Topic: Arrays, Two Pointers

Problem Link:
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Approach:
Sort both arrays and use two pointers to find common elements.
This handles duplicates correctly.

Time Complexity: O(n log n + m log m)
Space Complexity: O(1) (excluding output)
"""

class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        result = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result
