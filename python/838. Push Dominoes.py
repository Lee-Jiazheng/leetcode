"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""

# 记录下多少个'.'
class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        res = ""
        curr, cnt_dots = ".", 0
        for i, d in enumerate(dominoes):
            if d == ".":
                cnt_dots += 1
            elif d == "R":
                res += curr * cnt_dots + "R"
                curr = "R"
                cnt_dots = 0
            else:
                if curr != "R":
                    res += "L" * (cnt_dots+1)
                else:
                    res += "R" * (cnt_dots // 2)
                    if cnt_dots % 2 == 1:
                        res += "."
                    res += "L" * (cnt_dots // 2 + 1)    # current left char
            
                curr = "."
                cnt_dots = 0
        res += curr * cnt_dots
        return res
            
                
        