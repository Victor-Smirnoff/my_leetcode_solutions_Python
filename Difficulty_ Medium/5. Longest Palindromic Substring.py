# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring
# Given a string s, return the longest 
# palindromic substring  in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s):
        if s[0] * len(s) == s:
            return s
        if s == s[::-1]:
            return s

        res = []
        for i in range(len(s)):
            tmp = s[i]
            if tmp not in res:
                res.append(tmp)
            for j in range(i, len(s)):
                if i != j:
                    tmp += s[j]
                    if tmp == tmp[::-1] and tmp not in res:
                        res.append(tmp)
        res.sort(reverse=True, key=len)

        return res[0]
