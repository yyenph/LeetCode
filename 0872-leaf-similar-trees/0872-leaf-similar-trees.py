# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        return self.dfs_leaf(root1) == self.dfs_leaf(root2)
    
    def dfs_leaf(self,node):
        leaf_sequence = []
        if not node.left and not node.right:
            leaf_sequence.append(node.val)
        else:
            if node.left: 
                leaf_sequence.extend(self.dfs_leaf(node.left))
            if node.right:
                leaf_sequence.extend(self.dfs_leaf(node.right))
        return leaf_sequence
        
            
            
            
            
                    
            
        #use DFS
        #if !currentNode.left and !currentNode.right: append to result
        