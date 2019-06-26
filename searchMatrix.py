# -*- coding: utf-8 -*-
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        #遍历循环矩阵
        for i in range(0,len(matrix)):
            list=matrix[i]
        #对每个元素列表进行遍历
            for j in range(0,len(list)):
        #判断元素列表中的每个元素是否等于target
                if target==list[j]:
                    return True
        return False