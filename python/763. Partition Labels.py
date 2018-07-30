"""
 A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

"""

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        record = {}
        for i, c in enumerate(S):
            if c not in record:
                record[c] = [i, -1]
            else:
                record[c][1] = i
        partitions = []
        firstindex, lastindex = 0, 0
        while firstindex < len(S):
            i = lastindex = firstindex
            while i < len(S) and i <= lastindex:
                if record[S[i]][1] > lastindex:
                    lastindex = record[S[i]][1]
                i += 1
            partitions.append(lastindex - firstindex + 1)
            firstindex = lastindex + 1                
        return partitions