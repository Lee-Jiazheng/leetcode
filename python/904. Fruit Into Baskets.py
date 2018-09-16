"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
"""

# 滑动窗口的方式
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        count = {}
        i = res = 0
        
        for j, e in enumerate(tree):
            count[e] = count.get(e, 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            res = max(res, j-i+1)
        return res

class Solution:
    # TOL, 没有考虑010101010101的情况
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ct = [0 for _ in range(len(tree))]
        i = 0
        while i < len(tree):
            if i > 0:
                while i < len(tree) and tree[i] == tree[i-1]:
                    ct[i] = ct[i-1]-1
                    i += 1
            
            if i == len(tree):
                break
            a = {tree[i]}
            for j in range(i, len(tree)):
                a.add(tree[j])
                if len(a) == 3:
                    #ct[i] = j-i; break
                    j -= 1
                    break
            ct[i] = j + 1 - i
            i += 1
        #print(ct)
        return max(ct)