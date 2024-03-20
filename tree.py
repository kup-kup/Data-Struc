from collections import deque

class Tree:
  def __init__(self, root=None):
    self.root = root

class TreeNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def height(node):
  if node is None:
    return 0
  return max(height(node.right), height(node.left)) + 1

def count(node):
  if node is None:
    return 0
  return count(node.left) + count(node.right) + 1

def preorder(node):
  if node is not None:
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
  if node != None:
    inorder(node.left)
    print(node.data, end = " ")
    inorder(node.right)

def postorder(node):
  if node != None:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = " ")

def breadth(node):
  q = deque([node])

  while len(q) != 0:
    curr = q.pop()
    print(curr.data, end = " ")

    if curr.left != None:
      q.appendleft(curr.left)
    if curr.right != None:
      q.appendleft(curr.right)

tree1 = Tree(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4,)), TreeNode(5)))
#      1
#     / \
#    2   5
#   / \
#  3   4

tree2 = Tree(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(6))), TreeNode(5, TreeNode(7, TreeNode(8)))))

#      1
#     / \
#    2   5
#   / \  
#  3   4 7
#     6  8 

# print(height(tree1.root))
# print(height(tree2.root))
# print(count(tree1.root))
# print(count(tree2.root))

breadth(tree2.root)