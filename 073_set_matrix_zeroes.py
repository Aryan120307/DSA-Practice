"""
LeetCode 73 - Set Matrix Zeroes
Difficulty: Medium
Topic: Arrays, Matrix

Problem Link:
https://leetcode.com/problems/set-matrix-zeroes/

Approach:
Store rows and columns containing zero.
Then set entire row and column to zero.

Time Complexity: O(m * n)
Space Complexity: O(m + n)
"""

class Solution:
    def setZeroes(self, matrix):
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        # Step 1: Find zero positions
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Step 2: Set rows to zero
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0

        # Step 3: Set columns to zero
        for c in cols:
            for i in range(m):
                matrix[i][c] = 0
