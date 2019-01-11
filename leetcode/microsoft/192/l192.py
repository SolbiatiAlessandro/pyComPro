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
            left,right=node.left,node.right
            while left:
                left.next = right
                left = left.right
                right = right.left
        def solve(node):
            if node: connect_node(node)
            if node.left:
                solve(node.left)
                solve(node.right)
        solve(root)
        
if __name__ == "__main__":
    t = TreeLinkNode
    root = t(1)
    root.left = t(2)
    root.left.right = t(5)
    root.left.left = t(4)
    root.right = t(3)
    root.right.left = t(6)
    root.right.right = t(7)
    s=Solution()
    s.connect(root)
    assert root.next == None
    assert root.right.next == None
    assert root.left.next == root.right
    assert root.left.right.next == root.right.left
