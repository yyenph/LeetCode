from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        last_node = None
        while queue:
            levels= len(queue)
            for level in range(levels):
                current_node = queue.popleft()
                last_node = current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(last_node)
        return result
        
        