class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, head=None):
    self.head = head
    
  def print(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next
      
  def count(self):
    count = 0
    temp = self.head
    while temp is not None:
      count += 1
      temp = temp.next
    return count

class Stack(LinkedList):
  def __init__(self, head=None):
    self.head = head

  def is_empty(self):
    return self.head is None
  
  def push(self, node):
    node.next = self.head
    self.head = node

  def pop(self):
    if not self.is_empty():
      node = self.head
      self.head = self.head.next
      return node

class Tree:
  def __init__(self, root=None):
    self.root = root

class TreeNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def preorder(node):
  if node is not None:
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
  if node is not None:
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

def postorder(node):
  if node is not None:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")

input = "5 9 4 + 2 6 * - /"
input_list = input.split()

stack = Stack()
for i in input_list:
    if i in "+-*/":
        node = TreeNode(i)
        node.left = stack.pop()
        node.right = stack.pop()
        stack.push(node)
    else:
        stack.push(TreeNode(i))

root = stack.pop()

preorder(root)
print()
inorder(root)
print()
postorder(root)