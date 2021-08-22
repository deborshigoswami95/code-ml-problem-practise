# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        lo_traverse = [[root.val]]
        
        current_parents = [root]
        current_children = []
        
        while True:
            for node in current_parents:
                if node.left:
                    current_children.append(node.left)
                if node.right:
                    current_children.append(node.right)
            if current_children!=[]:
                lo_traverse.append([i.val for i in current_children])
                current_parents=current_children
                current_children=[]
            else:
                break
        
        return lo_traverse
