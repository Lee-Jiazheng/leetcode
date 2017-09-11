# 通过捕获异常的方式来判断是否能够reshape

def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(r):
            res.append([])
        try:
            col = row =  0
            for i in range(r):
                for j in range(c):
                    res[i].append(nums[row][col])
                    col += 1
                    if col == len(nums[row]):
                        row += 1
                        col  = 0
        except Exception as err:
            res = nums
        return res
