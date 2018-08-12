"""

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

# 动态规划
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        expression = re.split(r'([*+-])', input)
        if len(expression) == 1:
            return [int(expression[0])]
        return self.ways(expression, 0, len(expression)-1)
    
    def ways(self, expr, i, j):
        if i == j:
            return [expr[i]]
        result = []
        for opr in range(i+1, j, 2):    # 找到操作符
            left = self.ways(expr, i, opr-1)
            right = self.ways(expr, opr+1, j)
            for l in left:
                for r in right:
                    result.append(eval(str(l) + expr[opr] + str(r)))
        return result