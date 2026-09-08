# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_valid_bst(self, curr: Optional[TreeNode], lower: int, upper: int) -> bool:
        if curr is None:
            return True

        if not lower < curr.val < upper:
            print(lower, curr.val, upper)
            return False

        return self.check_valid_bst(curr.left, lower, curr.val) and self.check_valid_bst(curr.right, curr.val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_valid_bst(root, -math.inf, math.inf)