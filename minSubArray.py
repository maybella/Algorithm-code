# -*- coding: utf-8 -*-
# class Solution:
#     """
#     @param: nums: a list of integers
#     @return: A integer indicate the sum of minimum subarray
#     """
#     def minSubArray(self, nums):
#         # write your code here
#         minSum=nums[0]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 list=nums[i:j]
#                 tempSum=sum(list)
#                 if tempSum<minSum:
#                     minSum=tempSum
#         return minSum

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        minSum=nums[0]
        curSum=0
        for i in nums:
            curSum+=i
            if curSum<minSum:
                minSum=curSum
            if curSum>0:
                curSum=0
        return minSum