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
        node, stack, prev = root, [], None
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return True
        
