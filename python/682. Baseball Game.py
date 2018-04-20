# 简单， 主要是多种情况需要注意
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        _ops = []
        for op in ops:
            if op == "C":
                _ops.pop()
            elif op == "D":
                _ops.append(_ops[-1]*2)
            elif op == "+":
                _ops.append(_ops[-1]+_ops[-2])
            else: _ops.append(int(op))
        return sum(_ops)