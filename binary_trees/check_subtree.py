from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        while len(queue):
            node = queue.popleft()
            if node.val == subRoot.val:
                if checkTree(node,subRoot):
                    return True
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False



def checkTree(node, subNode):
    if not node and not subNode:
        return True
    elif not node or not subNode or node.val != subNode.val:
        return False
    return checkTree(node.left,subNode.left) and checkTree(node.right, subNode.right)
