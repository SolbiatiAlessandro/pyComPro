# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None''

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        def pre_order_traversal(node):
            if node is not None:
                pre_order_traversal(node.left)
                self.nodes.append(node.val)
                pre_order_traversal(node.right)
        self.pre_order_traversal(root)
        self.index = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.nodes)

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.nodes[self.index - 1]
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
