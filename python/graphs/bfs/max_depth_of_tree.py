# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        current_children = []
        current_parent = [root]
        depth = 1
        
        while True:
            for node in current_parent:
                if node.left:
                    current_children.append(node.left)
                if node.right:
                    current_children.append(node.right)
            if current_children!=[]:
                depth+=1
                current_parent=current_children
                current_children=[]
            else:
                break
                
        return depth
