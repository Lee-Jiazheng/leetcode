class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        for domain in cpdomains:
            time, d = domain.split(" ")
            ds = d.split(".")
            for i in range(len(ds)):
                res[".".join(ds[i:])] = res.get(".".join(ds[i:]), 0) + int(time)
        return ["%s %s" % (time, d) for d, time in res.items()]