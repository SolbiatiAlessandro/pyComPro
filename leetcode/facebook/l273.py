class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num: return 'Zero'
        num = str(num)
    
        nineteenmap = {0: '', 1:'One ',2:'Two ',3:'Three ',4:'Four ',5:'Five ',6:'Six ',7:'Seven ',8:'Eight ',9:'Nine ',10:'Ten ',11:'Eleven ',12:'Twelve ',13:'Thirteen ',14:'Fourteen ',15:'Fifteen ',16:'Sixteen ',17:'Seventeen ',18:'Eighteen ',19:'Nineteen '}
        tensmap = {0:'',2:'Twenty ',3:'Thirty ',4:'Forty ',5:'Fifty ',6:'Sixty ',7:'Seventy ',8:'Eighty ',9:'Ninety '}
        zerosmap = ['Hundred ','Thousand ','Million ','Billion ']
        
        def notrailzero(_digits):
            digits = ""
            for i in xrange(len(_digits)):
                if _digits[i] != '0':
                    digits = _digits[i:]
                    break
            return digits
        
        def two(digits):
            digits = notrailzero(digits)
            if not digits: return ""
            if len(digits) == 1 or\
                len(digits) == 2 and digits[0] == '1': return nineteenmap[int(digits)]
            if len(digits) == 2:
                return tensmap[int(digits[0])] + nineteenmap[int(digits[1])]
        
        def three(digits):
            digits = notrailzero(digits)
            if len(digits) < 3: return two(digits)
            return nineteenmap[int(digits[0])] + zerosmap[0] + two(digits[1:])
        
        res = ""
        if len(num) > 9 and three(num[:-9]):
            res += three(num[:-9]) + "Billion "
        
        if len(num) > 6 and three(num[-9:-6]):
            res += three(num[-9:-6]) + "Million "
        
        if len(num) > 3 and three(num[-6:-3]):
            res += three(num[-6:-3]) + "Thousand "
        
        res += three(num[-3:])
        return res[:-1]
        
        
                
            
            
            