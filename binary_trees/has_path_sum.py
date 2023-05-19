# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        targetSum -= root.val

        left = root.left
        right = root.right

        # if it's a leaf, check for equivalence
        if not left and not right: return targetSum == 0
        else: return self.hasPathSum(left, targetSum) or self.hasPathSum(right, targetSum)
