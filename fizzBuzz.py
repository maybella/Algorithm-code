# -*- coding: utf-8 -*-
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        l=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                #l.insert(len(l),"fizz buzz")
                l.append('fizz buzz')
            elif i%3==0:
                l.append('fizz')
                #l.insert(len(l),"fizz")
            elif i%5==0:
                l.append('buzz')
                #l.insert(len(l),"buzz")
            else:
                l.append(str(i))
                #l.insert(len(l),str(i))
        return l