# https://leetcode.com/problems/path-sum-ii/

from typing import Optional, Union, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        master_path_list = []

        def check_current_sum(node:TreeNode, current_sum:int, path_list:list) -> bool:
            if not node.left and not node.right and current_sum-node.val==0:
                master_path_list.append(path_list+[node.val])
                return True
            elif not node.left and not node.right and current_sum-node.val!=0:
                return False
            

            if node.left:
                left_check=check_current_sum(node.left,current_sum-node.val,path_list+[node.val])
            else:
                left_check=False
            if node.right:
                right_check=check_current_sum(node.right,current_sum-node.val,path_list+[node.val])
            else:
                right_check=False

            return left_check or right_check
        
        check_current_sum(root,targetSum,[])

        return master_path_list
    

####### BEST SOLUTION ################
#### https://leetcode.com/problems/path-sum-ii/solutions/484120/python-3-beats-100-nine-lines-dfs/?orderBy=most_votes&languageTags=python

class bestSolution:
    def pathSum(self, R: TreeNode, S: int) -> List[List[int]]:
        A, P = [], []
        def dfs(N):
            if N == None: return
            P.append(N.val)
            if (N.left,N.right) == (None,None) and sum(P) == S: A.append(list(P))
            else: dfs(N.left), dfs(N.right)
            P.pop()
        dfs(R)
        return A
