"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        c = collections.Counter(S)
        zeros = ones = 0
        S = "-" + S
        m = flip = len(S)
        dp = [None] * len(S)        
        for i, s in enumerate(S):
            if s == "0": zeros += 1
            elif s == "1": ones += 1
            print(zeros, ones, ones + c["0"] - zeros, m)
            if ones + c["0"] - zeros < m:
                flip = i
                m = ones + c["0"] - zeros
        return m
        return S[1:flip+1].replace("1", "0") + S[flip+1:].replace("0", "1")
            