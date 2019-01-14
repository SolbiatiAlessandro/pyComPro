class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        curr = root
        res, small = None, 1e9
        while curr.val != p.val:
            if curr.val > p.val and curr.val - p.val < small:
                res, small = curr, curr.val
            if curr.val < p.val:
                curr = curr.right
            else:
                curr = curr.left
                
        if not curr.right: return res
        curr = curr.right
        if curr.val > p.val and curr.val - p.val < small:
            res, small = curr, curr.val
        
        while curr.left:
            curr = curr.left
            if curr.val > p.val and curr.val - p.val < small:
                res, small = curr, curr.val
        
        return res
