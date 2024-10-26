# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def find_and_switch(node, cur_depth):
            if cur_depth == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
                return
            if node.left:
                find_and_switch(node.left, cur_depth + 1)
            if node.right:
                find_and_switch(node.right, cur_depth + 1)
                
    
        if depth == 1:
            root = TreeNode(val, left=root)
        else:
            find_and_switch(root, 1)
        return root