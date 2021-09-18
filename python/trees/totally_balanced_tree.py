"""
    Question:
    Given a binary tree, return whether or not the tree is totally balanced
    
    Define Total Balance: 
    Depth of left sub-tree == depth of right sub-tree for every node
    For the entire tree to be balanced, every node must be balanced

    Tree:
            3
           / \ 
          1   2
    solution: True

    Tree:
                3
               / \ 
              1   
    solution: False

    Tree:
                3
               / \ 
              1   2
            / |   | \ 
           4  5   6  7
    solution: True

    Tree:
                3
               / \ 
              1   2
            / |   | \ 
           4         7
    solution: False
"""

class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def check_tree_balance(node):
    if not node:
        return True

    if node.left and node.right:
        return bool(check_tree_balance(node.left) and check_tree_balance(node.right))
    elif not node.left and not node.right:
        return True
    else:
        return False


if __name__=="__main__":
    root=Node(2)
    root.left=Node(1)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(6)
    root.right.left=Node(5)
    root.right.right=Node(7)

    print(check_tree_balance(root))
