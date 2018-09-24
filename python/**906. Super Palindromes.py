

# 第一种解法
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        cans = []
        # repeat=5代表基础回文一半的长度
        # 10位数平方就是20位
        for a, b, c, d, e in itertools.product("0123", repeat=5):
            if int(a)**2 + int(b)**2 + int(c)**2 + int(d)**2 + int(e) **2 < 5:
                left = int(a+b+c+d+e)
                if left > 0:
                    cans.append(int(str(left)+str(left)[::-1]))
            
            if 2*(int(a)**2 + int(b)**2 + int(c)**2 + int(d)**2) + int(e) **2 < 10:
                left = int(a+b+c+d+e)
                if left > 0:
                    cans.append(int(str(left)+str(left)[::-1][1:]))
        
        cans.sort()
        i, j = 0, len(cans)-1
        while i < len(cans) and cans[i]**2 < int(L):
            i += 1
        while j > 0 and cans[j]**2 > int(R):
            j -= 1
        return j - i + 1
        

# 第二种解法
# 通过观察，所有的基础数字都只包含0/1/2，除了1,2,3。
class Solution:
    def superpalindromesInRange(self, L, R):

        R = int(R)
        L = int(L)
        
        sqrt_sp = ['11', '22']
        
        for i in sqrt_sp:
            for j in ('0','1','2'):
                sqrt_sp.append(str(i[:len(i)//2])+ j +str(i[len(i)//2:]))
            if int(i) **2 > R:
                break
        sqrt_sp.append(1)
        sqrt_sp.append(2)
        sqrt_sp.append(3)
        
        ans  = 0
				
        for i in sqrt_sp:
            s = int(i)**2
            if L <= s <= R and str(s) == str(s)[::-1]:
                ans +=1
        return ans