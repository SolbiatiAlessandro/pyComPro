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
        res = root.val
        while root:
            res = min((res, root.val), key=lambda x: abs(x - target))
            root = root.left if target < root.val else root.right
        return res
