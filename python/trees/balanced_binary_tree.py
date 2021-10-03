# https://leetcode.com/problems/balanced-binary-tree/


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_balance(root):
            if not root: return [True,0]
            
            left=check_balance(root.left)
            right=check_balance(root.right)
            
            balanced = left[0] and right[0] and (abs(left[1]-right[1]<=1))
            height = 1 + max(left[1], right[1])
            
            return [balanced, height]
        
        return check_balance(root)[0]
  
  
