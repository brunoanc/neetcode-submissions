# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, curr: Optional[TreeNode]) -> None:
        if curr is None:
            return

        curr.left, curr.right = curr.right, curr.left

        self.traversal(curr.left)
        self.traversal(curr.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
