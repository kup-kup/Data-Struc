class Tree:
  def __init__(self, root = None):
    self.root = root

class TreeNode:
  def __init__(self, data=None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

tree = Tree(TreeNode(5, right = TreeNode()))