class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        def gen():
            while True:
                yield from [i for i in range(numRows)] + [i for i in range(numRows-2, 0, -1)]
        g = gen()
        lst = [[] for _ in range(numRows)]
        for _s in s:
            lst[next(g)].append(_s)
        return "".join(list(itertools.chain(*lst)))