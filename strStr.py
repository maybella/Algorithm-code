# -*- coding: utf-8 -*-
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        #find方法
        #return source.find(target)
        try:
        	index=source.index(target) #index方法可以快速定位出第一个子字符串的首位置
        	return index
        except:
        	return -1   #index()方法在查询不到子字符串时会报错,利用该特性,返回处理.