class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A)==0:
            return 0
        for i in range(len(A)):
            if A[i]>=target:
                return i
        return len(A)