# https://leetcode.com/problems/path-sum/

from typing import Optional, Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        

        def check_current_sum(node:TreeNode, current_sum:int) -> Union[bool, TreeNode]:
            if not node.left and not node.right and current_sum-node.val==0:
                return True
            elif not node.left and not node.right and current_sum-node.val!=0:
                return False
            

            if node.left:
                left_check=check_current_sum(node.left,current_sum-node.val)
            else:
                left_check=False
            if node.right:
                right_check=check_current_sum(node.right,current_sum-node.val)
            else:
                right_check=False

            return left_check or right_check

        return check_current_sum(root,targetSum)