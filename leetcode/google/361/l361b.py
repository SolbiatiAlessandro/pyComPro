class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(start, end):
            """partition function from the quicksort

            Args:
                start, end : int, start and end of the partition to be computed
            Returns:
                partition_index: int, result of the partition
            """
            pivot = nums[end]
            partition_index = start - 1
            for index in xrange(start, end):
                if nums[index] <= pivot:
                    partition_index += 1
                    nums[partition_index], nums[index] = nums[index], nums[partition_index]
            nums[partition_index + 1], nums[end] = nums[end], nums[partition_index + 1]
            return partition_index + 1

        start, end = 0, len(nums) - 1
        while True:
            index = partition(start, end)
            if len(nums) - index == k:
                return nums[index]
            elif len(nums) - index > k:
                start = index + 1
            else:
                end = index - 1
