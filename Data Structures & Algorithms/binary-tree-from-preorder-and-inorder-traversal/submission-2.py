# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build_tree(self, curr: Optional[TreeNode], preorder_start: int, inorder_start: int, subtree_length: int):
        index = self.inorder_tree[curr.val]

        left_inorder_start = inorder_start
        left_preorder_start = preorder_start + 1
        len_left = index - left_inorder_start

        right_inorder_start = index + 1
        right_preorder_start = left_preorder_start + len_left
        len_right = subtree_length - len_left - 1

        if len_left > 0:
            curr.left = TreeNode(self.preorder[left_preorder_start])
            self.build_tree(curr.left, left_preorder_start, left_inorder_start, len_left)

        if len_right > 0:
            curr.right = TreeNode(self.preorder[right_preorder_start])
            self.build_tree(curr.right, right_preorder_start, right_inorder_start, len_right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder_tree = {x: i for i, x in enumerate(inorder)}
        root = TreeNode(preorder[0])
        self.build_tree(root, 0, 0, len(inorder))
        return root
