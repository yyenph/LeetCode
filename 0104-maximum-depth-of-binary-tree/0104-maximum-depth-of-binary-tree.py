# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            maxleft = self.maxDepth(root.left)
            maxright = self.maxDepth(root.right)
        return max(maxleft,maxright) + 1 # +1 for the current level of the treee