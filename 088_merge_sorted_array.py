"""
LeetCode 88 - Merge Sorted Array
Difficulty: Easy
Topic: Arrays, Two Pointers

Problem Link:
https://leetcode.com/problems/merge-sorted-array/

Approach:
Use three pointers starting from the end of both arrays.
Place the larger element at the end of nums1.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
