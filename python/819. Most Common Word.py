# Easy

# Counter most_common
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for s in "!?',;.": paragraph = paragraph.replace(s, "")
        from collections import Counter
        for word, _ in Counter(paragraph.lower().split(" ")).most_common():
            if word not in banned: return word