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

class Queue(LinkedList):
  def __init__(self, head=None):
    self.head = head
    self.tail = head

  def enqueue(self, node):
    self.tail.next = node
    self.tail = node

  def dequeue(self):
    temp = self.head.data
    self.head = self.head.next
    return temp

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

if __name__ == "__main__":
    queue = Queue(Node(2))
    queue.enqueue(Node(7))
    queue.enqueue(Node(4))
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(Node(5))
    queue.print()