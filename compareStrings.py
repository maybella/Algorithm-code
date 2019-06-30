class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        # write your code here
        #考虑A与B为空时,返回True
        # if A=='' and B=='':
        #      return True
        #在上面考虑了AB为空时,若A还空,B不空,返回False
        # if A=='':
        #     return False
        #该判断在处理A空,B不空的情况下,快速淘汰A元素个数少于B元素个数的情况
        # if len(A)<len(B):
        #     return False
        #在能判断A,B都为空时返回True的前提下,快速淘汰A,B个数相同时,元素是否能一一对应
        if len(A)==len(B):
            return (sorted(A)==sorted(B))
        #在处理A,B空的情况下,对B中每个元素i进行判断:B中i元素的个数>A中i元素的个数,return False
        for i in B:
            # if i not in A:
            #     return False
            if A.count(i)<B.count(i):
                return False
        return True