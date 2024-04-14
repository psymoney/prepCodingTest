import sys

sys.setrecursionlimit(1000)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def go_and_sum(node, side=None):
            sum = 0
            if not node.left and not node.right and side == 'l':
                return node.val
            if node.left:
                sum += go_and_sum(node.left, 'l')
            if node.right:
                sum += go_and_sum(node.right, 'r')
                
            return sum

        return go_and_sum(root)
                
            