# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        return self.dfs_leaf(root1) == self.dfs_leaf(root2)
    
    # def dfs_leaf(self,node):
    #     leaf_sequence = []
    #     if not node.left and not node.right:
    #         leaf_sequence.append(node.val)
    #     else:
    #         if node.left: #extend the leaf_sequence from each call
    #             leaf_sequence.extend(self.dfs_leaf(node.left))
    #         if node.right:
    #             leaf_sequence.extend(self.dfs_leaf(node.right))
    #     return leaf_sequence
    #solution2: using Stack
    def dfs_leaf(self,node):
        leaf_sequence = []
        stack = [node]
        while stack:
            currentNode = stack.pop()
            if currentNode.left:
                stack.append(currentNode.left)
            if currentNode.right:
                stack.append(currentNode.right)
            if not currentNode.left and not currentNode.right:
                leaf_sequence.append(currentNode.val)
        return leaf_sequence
            
            
            
            
                    
            
        #use DFS
        #if !currentNode.left and !currentNode.right: append to result
        