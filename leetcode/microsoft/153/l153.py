# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        stack = [root]
        while root.left:
            root = root.left
            stack.append(root)
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                curr = curr.right
                stack.append(curr)
                while curr.left:
                    curr = curr.left
                    stack.append(curr)
        return res


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    s=Solution()
    assert s.inorderTraversal(tree) == [1,3,2]
    assert s.inorderTraversal(TreeNode(1)) == [1]
    assert s.inorderTraversal(None) == []

