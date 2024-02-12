from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Edge case: Root has no children
        if ((not root.left) and (not root.right)):
            return True

        ll = []
        self.preOrderTraversal(root, ll)
        print(ll)
        return ll[:len(ll)//2+1] == ll[len(ll)//2:][::-1]

    # Pre-order traversal: Left, Parent, Right
    def preOrderTraversal(self, cur, t_list):
        if (not cur):
            t_list.append(None)
        else:
            self.preOrderTraversal(cur.left, t_list)
            t_list.append(cur.val)
            self.preOrderTraversal(cur.right, t_list)
