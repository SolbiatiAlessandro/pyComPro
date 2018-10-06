 #Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        prev, curr = None, root
        while curr.val != p.val:
            if curr.val > p.val:
                prev = curr
                curr = curr.left
            else:
                curr = curr.right
        res, curr = None, curr.right
        while curr:
            res = curr
            curr = curr.left
        return res if res is not None else prev

