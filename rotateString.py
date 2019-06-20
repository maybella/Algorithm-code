# -*- coding: utf-8 -*-
class Solution:
    """
    @param str: An array of char  字符串数组
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if len(str)==0 or offset==0:
            return str
        for i in range(offset%len(str)):
            str.insert(0,str.pop())
        return str