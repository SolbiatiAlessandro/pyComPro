# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        res = [[root.val]]
        queue = [(root, 0)] 
        while queue:
            curr, depth = queue.pop()
            def res_append(node):
                if len(res) == depth + 1: res.append([node.val])
                else: res[depth + 1].append(node.val)
                queue.insert(0, (node, depth + 1))
            if curr.left: res_append(curr.left)
            if curr.right: res_append(curr.right)
        for i, level in enumerate(res):
            if i%2==1: res[i] = level[::-1]
        return res


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    s=Solution()
    assert s.zigzagLevelOrder(tree) == [[3],[20,9],[15,7]]
    assert s.zigzagLevelOrder(None) == []
    assert s.zigzagLevelOrder(TreeNode(1)) == [[1]]
