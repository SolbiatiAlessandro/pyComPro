class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ksorted = []  
        if k - 1 < len(nums)/2:  #descending order
            for num in nums:
                if not ksorted or num >= ksorted[0]:
                    ksorted.insert(0, num)
                elif num <= ksorted[-1]:
                    ksorted.append(num)
                else:
                    a, b = 0, len(ksorted) - 1
                    while True:
                        m = (b-a)/2 + a
                        if ksorted[m+1] <= num <= ksorted[m]:
                            ksorted.insert(m+1, num)
                            break
                        elif ksorted[m] > num:
                            a = m
                        else:
                            b = m
                if len(ksorted) > k:
                    ksorted.pop()
        else:  #ascending order
            for num in nums:
                if not ksorted or num <= ksorted[0]:
                    ksorted.insert(0, num)
                elif num >= ksorted[-1]:
                    ksorted.append(num)
                else:
                    a, b = 0, len(ksorted)
                    while True:
                        m = (b-a)/2 + a
                        if ksorted[m] <= num <= ksorted[m+1]:
                            ksorted.insert(m+1, num)
                            break
                        elif ksorted[m] > num:
                            b = m
                        else:
                            a = m
                if len(ksorted) > len(nums) + 1 - k:
                    ksorted.pop()
        return ksorted[-1]
