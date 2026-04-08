"""
LeetCode 121 - Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Arrays, Greedy

Problem Link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
Track the minimum price seen so far and calculate profit at each step.
Update maximum profit accordingly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
