class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while i!=-1:
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
            i-=1
        return [1]+digits
