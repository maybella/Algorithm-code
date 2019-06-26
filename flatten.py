class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def __init__(self) :
        self.L = []
    def flatten(self, nestedList):
        # Write your code here
        for i in range(0,len(nestedList)):
            if isinstance(nestedList[i],list):
                self.flatten(nestedList[i])
            else:
                self.L.append(nestedList[i])
        return self.L