class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

def max_depth(node):
    if not node:
        print('tree end')
        return 0

    left_depth=max_depth(node.left)
    right_depth=max_depth(node.right)

    if left_depth>right_depth:
        print('At node {} and max depth is {} on the left'.format(node.val, left_depth+1))
        return left_depth+1
    else:
        print('At node {} and max depth is {} on the right'.format(node.val, right_depth+1))
        return right_depth+1


if __name__=="__main__":
    root=Node(3)
    root.left=Node(1)
    root.right=Node(5)
    root.right.left=Node(4)
    root.right.right=Node(7)
    root.right.right.left=Node(6)
    root.right.right.right=Node(8)
    print(max_depth(root))
