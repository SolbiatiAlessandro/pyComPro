class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def inorder(node):
            if not node: return ""
            return str(node.val) +\
                    inorder(node.left) +\
                    inorder(node.right)

        def preorder(node):
            if not node: return ""
            return preorder(node.left) +\
                   str(node.val) +\
                   preorder(node.right)

        return inorder(root) + preorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recurr(a, b, c, d):
            res = TreeNode(data[a])
            if a == b: return res
            for i in xrange(c, d + 1):
                if data[i] == data[a]:
                    res.left = recurr(a + 1, a + i - c, c, i - 1)
                    res.right = recurr(a + i - c + 1, b, i + 1, d)
            return res
        
        return recurr(0, len(data) / 2 - 1, len(data) / 2, len(data) - 1)




if __name__ == "__main__":
    tree = TreeNode(5)
    tree.right = TreeNode(7)
    tree.right.right = TreeNode(8)
    tree.right.left = TreeNode(6)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(4)
    c = Codec()
    s = c.serialize(tree)
    print s
    res = c.deserialize(s)
