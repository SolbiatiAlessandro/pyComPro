# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root: root.next = None
        def connect_node(node):
            curr = node.next
            while (node.left or node.right) and curr and not (curr.left or curr.right):
                curr = curr.next
            _next = None if not curr else curr.left or curr.right
            if node.left: node.left.next = node.right or _next
            if node.right: node.right.next = _next
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr:
                connect_node(curr)
                queue.insert(0, curr.right)
                queue.insert(0, curr.left)

        
if __name__ == "__main__":
    t = TreeLinkNode
    root = t(1)
    root.left = t(2)
    root.left.right = t(5)
    root.left.left = t(4)
    root.right = t(3)
    root.right.right = t(7)
    s=Solution()
    s.connect(root)
    assert root.next == None
    assert root.right.next == None
    assert root.left.next == root.right
    assert root.left.right.next == root.right.right
