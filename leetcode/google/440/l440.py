def binary_search(nums, value):
    """
    binary_search the index of value in ordered nums,
    with interval of the kind [start, end)

    Args:
        nums: list(int)
        value: int
    Return:
        m: int, index of value in nums
    """
    if not nums or value < nums[0]: return - 1
    if value >= nums[-1]: return len(nums) - 1
    a, b = 0, len(nums) - 1
    while True:
        m = (b-a)/2 + a
        if nums[m] <= value < nums[m + 1]: return m
        elif value >= nums[m + 1]: a = m + 1
        else: b = m


class RangeModule(object):
    
    def __init__(self):
        self.nums = []

    def modifyRange(self, left, right, addRange):
        """helper for addRange/removeRange functions

        Args:
            addRange: bool, 1 if addRange, 0 if removeRange
        """
        left_index = binary_search(self.nums, left)
        right_index = binary_search(self.nums, right)
        if right_index % 2 == addRange:
            self.nums.insert(right_index + 1, right)
        if left_index % 2 == addRange and self.nums[left_index] != left:
            self.nums.insert(left_index + 1, left)
            left_index += 1
            right_index += 1
        del self.nums[left_index + 1: right_index + 1]


    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.modifyRange(left, right, 1)


    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        left_index = binary_search(self.nums, left)
        right_index = binary_search(self.nums, right - 1)
        if left_index % 2 == 1: return False
        if right_index == left_index: return True
        return False


    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.modifyRange(left, right, 0)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
