# 拼接list达到效果，如果长度不一致，一个添加0来凑即可。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        _l1, _l2 = l1, l2
        carry = 0
        while True:
            _l1.val += _l2.val + carry
            carry = 0
            if _l1.val >= 10: carry = 1; _l1.val = _l1.val - 10
            if _l1.next is None and _l2.next is None and not carry: break;
            if _l1.next is None: _l1.next = ListNode(0)
            if _l2.next is None: _l2.next = ListNode(0)
            
            _l1, _l2 = _l1.next, _l2.next
        return l1