class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i==j:
                    continue 
                tempSum=numbers[i]+numbers[j]
                if tempSum==target:
                    return [i,j]