class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here

        list=s.split(' ')
        list.reverse()
        l=''
        for i in list:
            if i!='':
                l+=i+' '
        a=l.rstrip()
        return a