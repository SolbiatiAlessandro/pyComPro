class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            cnt, number = 7, data[i]
            while cnt >= 0 and number&(1<<cnt): cnt -= 1
            if cnt < 3: return False
            repeat = 7 - cnt - 1
            if repeat == 0 and number & (1 << 7): return False
            while repeat > 0:
                i, repeat = i + 1, repeat - 1
                if i == len(data): return False
                if not( data[i] & (1 << 7) and
                        not data[i] & (1 << 6) ):
                    return False
            i += 1
        return True
