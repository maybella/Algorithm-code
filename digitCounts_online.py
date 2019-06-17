class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here 
        count=0
        if k==0:
            count=count+1
        for i in range(n+1):
            while(i!=0):
                j=i%10
                if j==k:
                    count=count+1
                i=i//10
        return count