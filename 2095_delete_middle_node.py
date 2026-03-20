"""
LeetCode 2095 - Delete the Middle Node of a Linked List
Difficulty: Medium
Topic: Linked List, Two Pointers

Problem Link:
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Approach:
Use slow and fast pointers to find the middle node.
Keep track of previous node to remove the middle.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
