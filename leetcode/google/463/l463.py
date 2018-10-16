"""Definition for a binary tree node."""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        big, small = None, None
        while root:
            if root.val == target:
                return root.val
            elif root.val > target:
                big = min(root.val, big) if big is not None else root.val
                root = root.left
            else:
                small = max(root.val, small)
                root = root.right
        if big is None: return small
        if small is None: return big
        if big - target < target - small: return big
        return small
