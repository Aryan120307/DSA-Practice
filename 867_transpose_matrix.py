"""
LeetCode 867 - Transpose Matrix
Difficulty: Easy
Topic: Arrays, Matrix

Problem Link:
https://leetcode.com/problems/transpose-matrix/

Approach:
Create a new matrix of size n x m and swap rows with columns.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # create empty matrix of size n x m
        result = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]

        return result
