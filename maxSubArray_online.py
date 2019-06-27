# -*- coding:utf-8 -*-
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        # 从i开始求和，如果当前和大于maxSum,则赋值给maxSum
        maxSum=nums[0]
        curSum=0
        for i in nums:
            curSum+=i
            if curSum>maxSum:
                maxSum=curSum
         # 前面的和如果已经小于0了，那么加上下一个元素值，肯定是小于下一个元素值
         # 所以如果前面加起来的值小于0了，则舍弃前面的和，从下一位开始继续求和
            if curSum<0:
                curSum=0
        return maxSum
# lists = [0, 1, 2, 3, -4, 5, 6]
# print(function(lists))