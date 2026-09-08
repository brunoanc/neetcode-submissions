# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs_func(self, curr: Optional[TreeNode]) -> None:
        if curr is None:
            return

        temp = curr.left
        curr.left = curr.right
        curr.right = temp

        self.bfs_func(curr.left)
        self.bfs_func(curr.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.bfs_func(root)
        return root
