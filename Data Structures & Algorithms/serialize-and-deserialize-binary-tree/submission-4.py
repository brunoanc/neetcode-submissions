from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        s = ""

        while q:
            node = q.popleft()

            if node is None:
                s += "n,"
                continue
            else:
                s += str(node.val)
                s += ","

            q.append(node.left)
            q.append(node.right)

        return s.rstrip("n,")

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        data_arr = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque([root])
        index = 1

        while q:
            node = q.popleft()

            if index < len(data_arr) and data_arr[index] != "n":
                node.left = TreeNode(int(data_arr[index]))
                q.append(node.left)

            if index + 1 < len(data_arr) and data_arr[index + 1] != "n":
                node.right = TreeNode(int(data_arr[index + 1]))
                q.append(node.right)

            index += 2

        return root
