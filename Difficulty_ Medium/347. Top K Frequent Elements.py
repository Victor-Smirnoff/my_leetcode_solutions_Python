# https://leetcode.com/problems/top-k-frequent-elements/description/
# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums, k):
        elem = sorted(set(nums))
        d = {}
        for i in range(len(elem)):
            d[elem[i]] = nums.count(elem[i])
            
        return [x[0] for x in sorted(d.items(), key=lambda x: x[1], reverse=True)][:k]
