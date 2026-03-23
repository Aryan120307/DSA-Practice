"""
LeetCode 4 - Median of Two Sorted Arrays
Difficulty: Hard
Topic: Arrays

Problem Link:
https://leetcode.com/problems/median-of-two-sorted-arrays/

Approach:
Merge both sorted arrays and then find the median.

Time Complexity: O(m + n)
Space Complexity: O(m + n)
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)

        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
