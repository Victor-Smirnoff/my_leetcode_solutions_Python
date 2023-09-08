# https://leetcode.com/problems/valid-palindrome/description/
# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def isPalindrome(self, s):
        s = [x for x in s.lower() if x in "abcdefghijklmnopqrstuvwxyz0123456789"]
        N = len(s) - 1
        left = 0
        rigth = N
        while left < rigth:
            if s[left] != s[rigth]:
                return False
            else:
                left += 1
                rigth -= 1

        return True
