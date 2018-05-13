class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return " ".join([rotate(s, i) for i, s in enumerate(S.split(" "), 1)])
    
def rotate(s, i):
    if s[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return s + "ma" + "a"*i        
    else:
        return s[1:] + s[0] + "ma" + "a"*i
        
