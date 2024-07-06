# Tree DFS Template
# Problem: Binary Tree Inorder Traversal

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: TreeNode) -> List[int]:
    result = []
    
    def dfs(node: TreeNode):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

# Unit tests
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

assert inorder_traversal(root) == [1, 3, 2]
