'''
ให้แสดงค่าภายในต้นไม้โดยใช้การแสดงแบบ pre-order, in-order, post-order ผสมกันแบบ recursive
โดยมีเงื่อนไขดังนี้
    - pre-order เมื่อต้นไม้ย่อยทางซ้ายสูงกว่าทางขวา
    - in-order เมื่อมีความสูงเท่ากัน
    - post-order เมื่อต้นไม้ย่อยทางซ้ายเตี้ยกว่าทางขวา
'''

class Tree:
  def __init__(self, root=None):
    self.root = root

class TreeNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def preorder(node: TreeNode) -> None:
  if node is not None:
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node: TreeNode) -> None:
  if node != None:
    inorder(node.left)
    print(node.data, end = " ")
    inorder(node.right)

def postorder(node: TreeNode) -> None:
  if node != None:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = " ")

def height(node: TreeNode, h = 1) -> int:
  if node.right == None and node.left == None:
    return h

  if node.right != None:
    right = height(node.right, h + 1)
  else:
    right = h

  if node.left != None:
    left = height(node.left, h + 1)
  else:
    left = h

  count = max(1, right, left)
  return count

def print_tree(node: TreeNode) -> None:
    if node is None:
        return None
  
    h_left = height(node.left) if node.left is not None else 0
    h_right = height(node.right) if node.right is not None else 0

    if h_left > h_right:
        print(node.data, end=" ")
        print_tree(node.left)
        print_tree(node.right)
    elif h_left == h_right:
        print_tree(node.left)
        print(node.data, end=" ")
        print_tree(node.right)
    elif h_left < h_right:
        print_tree(node.left)
        print_tree(node.right)
        print(node.data, end=" ")

tree1 = Tree(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5)))
#      1
#     / \
#    2   5
#   / \
#  3   4
tree2 = Tree(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(6, TreeNode(7)))), TreeNode(5)))
#      1
#     / \
#    2   5
#   / \
#  3   4
#     /
#    6
#   /
#  7

print_tree(tree1.root)
print()
print_tree(tree2.root)