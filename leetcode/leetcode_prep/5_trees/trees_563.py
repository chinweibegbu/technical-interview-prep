from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.parse(root, 0)[1]
    
    def parse(self, cur, tilt):
        if not cur:
            return ([], 0)
        else:
            left, right = self.parse(cur.left, tilt), self.parse(cur.right, tilt)
            new_tilt = left[1] + right[1] + abs(sum(left[0]) - sum(right[0]))
            new_children = [cur.val] + left[0] + right[0]
            return (new_children, new_tilt)