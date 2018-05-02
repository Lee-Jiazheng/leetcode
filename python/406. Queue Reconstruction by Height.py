# https://leetcode.com/problems/queue-reconstruction-by-height/description/


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda a: [a[0],-a[1]],reverse = True)
        result = []
        for p in people:
            result.insert(p[1], p)
        return result