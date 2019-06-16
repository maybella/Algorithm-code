import sys
sys.setrecursionlimit(1000000)
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
    #定义一个阶乘函数,输入n返回n阶乘的结果
        def jiecheng(n):
            if n==1:
            	return 1
            else:
            	return n*jiecheng(n-1)
    #把n阶乘的结果转换为字符串
        strres=str(jiecheng(n))
    #把字符串颠倒过来
        strres=strres[::-1]
        count=0
    #从前开始匹配'0',遇到个数加1,不匹配0时结束
        for x in strres:
            if x=='0':
                count=count+1
            else:
                break;
        return counts