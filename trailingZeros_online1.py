# -*- coding: utf-8 -*
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
    #先算n!的阶乘
        sum=1
        for x in range(1,n+1):
            sum=sum*x
    #利用sum%10==0计算0的个数
        count=0
        while(sum%10==0):
            count=count+1
            sum=sum//10 #需要整除符号('//'),取他的商为下次运算
        return count