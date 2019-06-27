# -*- coding: utf-8 -*-
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        #初始令最大值总和等于列表
        max=sum(nums)
        #循环数组range(0,len(nums))
        for i in range(len(nums)):
        #循环数组range(i+1,len(nums)+1),令j至少大于i的值为1.方便切片
            for j in range(i+1,len(nums)+1):
        #产生所有的子数组,并计算子数组的总和比较
                list=nums[i:j]
                temp=sum(list)
                if temp>max:
                    max=temp
        return max
