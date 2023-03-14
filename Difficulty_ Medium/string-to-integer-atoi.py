# https://leetcode.com/problems/string-to-integer-atoi/description/
# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

class Solution:
    def myAtoi(self, s: str) -> int:
        acceptable_range = range(-2147483648, 2147483647)
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0].isdigit() == False and s[0] != '-' and s[0] != '+':
            return 0

        res = []
        if s[0] == '-':
            res.append(s[0])
            for i in range(1, len(s)):
                if s[i].isdigit():
                    res.append(s[i])
                else:
                    break
        elif s[0] == '+':
            for i in range(1, len(s)):
                if s[i].isdigit():
                    res.append(s[i])
                else:
                    break
        else:
            for i in range(len(s)):
                if s[i].isdigit():
                    res.append(s[i])
                else:
                    break
        if res == []:
            return 0
          
        res2 = int(''.join(res)) if res != ['-'] else 0
        
        return res2 if res2 in acceptable_range else (-2147483648 if res2 < 0 and res2 not in acceptable_range else 2147483647)
