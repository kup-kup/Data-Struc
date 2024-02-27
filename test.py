class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def detect_cycle(self):
    tortoise = self.head.next
    hare = self.head.next.next

    while tortoise != hare:
      if hare.next == None or hare.next.next == None:
        return False
      tortoise = tortoise.next
      hare = hare.next.next
    return True

test = [2, 3, 6, 0, 4, 1, 5, 3]

ls = LinkedList(Node(3, Node(0, Node(2, Node(6, Node(5, Node(1, Node(3 , None))))))))

temp = ls.head

while temp.next != None:
  temp = temp.next

temp.next = ls.head.next

print(ls.detect_cycle())