class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shifts.reverse()
        for i in range(1, len(shifts)):
            shifts[i] = shifts[i-1]+shifts[i]
        def s(ch):
            i, ch = ch
            return chr((ord(ch) - ord('a') + shifts[len(shifts)-i-1]) % 26 + ord('a'))
        return "".join(list(map(s, enumerate(S))))