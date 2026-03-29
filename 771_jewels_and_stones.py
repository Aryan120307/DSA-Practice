"""
LeetCode 771 - Jewels and Stones
Difficulty: Easy
Topic: Strings, Hash Set

Problem Link:
https://leetcode.com/problems/jewels-and-stones/

Approach:
Convert jewels into a set for fast lookup.
Count how many stones are present in the set.

Time Complexity: O(n)
Space Complexity: O(m)
"""

class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1

        return count
