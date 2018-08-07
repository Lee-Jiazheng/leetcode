"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# 如果存在环，那么一个指针移动一个，另外一个移动两个，两个指针会相遇的

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        l1, l2 = head, head.next
        while l1 and l2 and l2.next:
            if l1 == l2: return True
            l1 = l1.next
            l2 = l2.next.next
        return False