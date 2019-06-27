class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        #set函数过滤列表元素
        temp=set(nums)
        for i in temp:
            #统计元素个数
            tempSum=nums.count(i)
            #当个数大于列表长度的一半,即为主元素
            if tempSum>=(len(nums)/2):
                return i
        return False

#字典处理
# class Solution:
#     """
#     @param: nums: a list of integers
#     @return: find a  majority number
#     """
#     def majorityNumber(self, nums):
#         # write your code here
#         dict={}
#         for i in nums:
#             if i not in dict.keys():
#                 dict[i]=1
#             else:
#                 dict[i]+=1
#         for i in dict.keys():
#             if dict[i]>=len(nums)/2:
#                 return i