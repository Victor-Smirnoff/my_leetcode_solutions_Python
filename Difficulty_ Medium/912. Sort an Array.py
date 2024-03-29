# https://leetcode.com/problems/sort-an-array/description/
# 912. Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

class Solution:
    def sortArray(self, nums):
        def merge_list(a, b):
            c = []
            N = len(a)
            M = len(b)

            i = 0
            j = 0
            while i < N and j < M:
                if a[i] <= b[j]:
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1

            c += a[i:] + b[j:]
            return c

        def split_and_merge_list(a):
            N1 = len(a) // 2
            a1 = a[:N1]
            a2 = a[N1:]

            if len(a1) > 1:
                a1 = split_and_merge_list(a1)
            if len(a2) > 1:
                a2 = split_and_merge_list(a2)

            return merge_list(a1, a2)

        return split_and_merge_list(nums)
