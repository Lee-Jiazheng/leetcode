class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for _s in s:
            if _s in "{[(":
                stack.append(_s)
            else:
                if len(stack) == 0: return False
                _p = stack.pop()
                if _p + _s not in ["[]", "{}", "()"]:
                    return False
        if len(stack) != 0: return False
        return True