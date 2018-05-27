"""

This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
"""

# 重点是，找到与当前查看字符串匹配的字符串个数。
# 比如这个字符串与密码匹配为2, 那么从集合中找到与这个字符串匹配2次的字符串。

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        from collections import defaultdict
        
        matches = defaultdict(lambda: defaultdict(set))
        n = len(wordlist)
        for i in range(n):
            for j in range(i+1, n):
                m_count = sum([1 for k in range(6) if wordlist[i][k] == wordlist[j][k]])
                matches[wordlist[i]][m_count].add(wordlist[j])
                matches[wordlist[j]][m_count].add(wordlist[i])
        print(matches)
        wordlist = set(wordlist)
        for i in range(10):
            guess = wordlist.pop()
            res = master.guess(guess)
            print(guess, res)
            if res == 6:
                return guess
            wordlist.intersection_update(matches[guess][res])