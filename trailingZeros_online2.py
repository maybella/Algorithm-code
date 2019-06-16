# -*- coding: utf-8 -*-
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        num=0
        while(n):
            num=num+n//5 #第一次循环计算出n中5的倍数的个数,第二次计算出25(5的2次方)的倍数的个数,如此类推
            n=n//5 #作为循环变化的条件,当你n<5的时候,就会置0结束循环
        return num
        
        