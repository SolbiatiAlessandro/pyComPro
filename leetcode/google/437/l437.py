"""Definition for a binary tree node."""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, prev = [], None
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                if prev is not None and root.val <= prev:
                    return False
                prev = root.val
                root = root.right
            else:
                return True
