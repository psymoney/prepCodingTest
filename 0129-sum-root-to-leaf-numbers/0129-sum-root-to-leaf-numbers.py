# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursive(node, num):
            num += str(node.val)
            result = 0
            
            if not node.left and not node.right:
                return int(num)
            
            if node.left:
                result += recursive(node.left, num)
            if node.right:
                result += recursive(node.right, num)
                
            return result
        
        return recursive(root, '')