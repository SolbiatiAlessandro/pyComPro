class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def assignDepth( node, value, depth ):
    """
    assign Depth value to everynode with a pre-order traversal recursive call
    to be called like this : assignDepth( root, -1, -1 )
    """
    if node is not None:
        node.depth = depth + 1 if node.val == value else 0 
        assignDepth( node.right, node.val, node.depth )
        assignDepth( node.left, node.val, node.depth )

def computeMax( node, res ):
    """
    compute max length with a post-order traversal recursive call
    to be called like this : computeMax( root, 0 )
    :rtype (int) result
    """
    if node is not None:
        res = max(  res, 
                    node.depth, 
                    computeMax( node.left, res ), 
                    computeMax( node.right, res ) )

        leftDepth = node.left.depth if node.left is not None else 0
        leftValue = node.left.val if node.left is not None else -1
        rightDepth = node.right.depth if node.right is not None else 0
        rightValue = node.right.val if node.right is not None else -1

        #import pdb;pdb.set_trace()
        if( node.val == rightValue == leftValue ):
            res = max( res, (rightDepth - node.depth) + (leftDepth - node.depth) )
            node.depth = max( rightDepth, leftDepth )
        elif( node.val == leftValue ):
            node.depth = leftDepth
        elif( node.val == rightValue ):
            node.depth = rightDepth

        return res

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        assignDepth( root, -1 , -1 )
        return computeMax( root, 0 )
