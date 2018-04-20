class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        res = []
        
        def next(n, r):
            if n == target: res.append(r); return
            if len(graph[n]) == 0: return 
            for ele in graph[n]:
                next(ele, r + [ele])
            
        for s in graph[0]:
            next(s, [0, s])
        return res