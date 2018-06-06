"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        h = r
        _h1, _h2 = l1, l2
        while _h1 or _h2:
            if _h1 is None:
                r.next = _h2; break
            elif _h2 is None:
                r.next = _h1; break
            
            if _h1.val >= _h2.val:
                r.next = ListNode(_h2.val); _h2 = _h2.next
            elif _h1.val < _h2.val:
                r.next = ListNode(_h1.val); _h1 = _h1.next
            r = r.next
        return h.next