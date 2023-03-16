# https://leetcode.com/problems/longest-common-prefix/
# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs):
        strs = sorted(strs, key=len)
        if len(strs) == 1:
            return strs[0]
        else:
            flag = True
            res = ''
            first = strs[0]
            for j in range(len(first)):
                count = 1
                for i in range(1, len(strs)):
                    if first[j] == strs[i][j]:
                        count += 1
                        if count == len(strs):
                            res += res.join(first[j])
                        continue
                    else:
                        flag = False
                        break
                if flag == False:
                    break

            return res
