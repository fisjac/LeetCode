# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: #base case
            return root
        # print(root.val)


        # Action
        # print(root.left.val, root.right.val)
        root.left, root.right = root.right, root.left
        # print(root.left.val, root.right.val)

        # recursive step
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
