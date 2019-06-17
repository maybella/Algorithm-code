# -*- coding: utf-8 -*-
class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here 
        strk=str(k)
        count=0
        for i in range(0,n+1):
            stri=str(i)
            for j in stri:
                if j==strk:
                    count=count+1
        return count
