class Solution(object):
    def inorderSuccessor(self, root, p, lastres = None):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return lastres
        return self.inorderSuccessor(root.right, p, lastres) if root.val <= p.val else self.inorderSuccessor(root.left, p, root)
