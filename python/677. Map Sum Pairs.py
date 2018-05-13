# 难点： 如果已经存在在列表中则需要替换， 则本次val为两次value差值。
# 加速方法： 设置count属性，则O(1)复杂度取，因为过程中会多次进行sum操作。

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.records = {}
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.keys: val = val - self.keys[key]; self.keys[key] = val
        r = self.records
        for k in key:
            if k not in r : r[k] = {} 
            r = r[k]
            r["count"] = r.get("count", 0) + val
        self.keys[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        r = self.records
        s = 0
        for p in prefix:
            r = r.get(p, None)
            if r is None: return 0
        return r["count"]
                    
def sum_tree(r, s=0):
    for k in r:
        if k == "_": s += r[k]
        else: s += sum_tree(r[k])
    return s

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)