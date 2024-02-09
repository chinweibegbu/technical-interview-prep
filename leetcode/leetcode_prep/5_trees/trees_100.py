from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Edge case: Both trees are empty
        if ((not p) and (not q)):
            return True
        # Edge case: Only one of both trees is empty
        elif ((p) and (not q)) or ((not p) and (q)):
            return False
        
        # General case: Each tree has at least one node
        p_list, q_list = [], []
        self.traverse(p, p_list)
        self.traverse(q, q_list)

        for x, y in zip(p_list, q_list):
            if (x != y):
                return False
        return True

    # Pre-order Traversal (Parent, Left, Right)
    def traverse(self, cur, tree_list):
        if (cur):
            tree_list.append(cur.val)
            self.traverse(cur.left, tree_list)
            self.traverse(cur.right, tree_list)
        else:
            tree_list.append(None)
