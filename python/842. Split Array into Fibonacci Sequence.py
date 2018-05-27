"""
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""


class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def first_zero(num):
            return len(num) != 1 and num[0] == '0'
        def find(_S, num1, num2):
            res = []
            while _S:
                _num = str(num1+num2)
                i = _S.find(_num)
                if i == -1 or i != 0:
                    return None
                else:
                    num1 = num2
                    num2 = int(_S[:len(_num)])
                    if num2 > pow(2, 31) - 1: return None
                    _S = _S[len(_num):]
                    res.append(num2)
            return res
        
        for i in range(1, len(S)-1):
            one = S[:i]
            for j in range(i+1, len(S)):
                two = S[i:j]
                if first_zero(one) or first_zero(two) or len(S[j:])<len(str(int(one)+int(two))):
                    continue
                res = find(S[j:], int(one), int(two))
                if res:
                    return [int(one), int(two)] + res
        return []
        
            