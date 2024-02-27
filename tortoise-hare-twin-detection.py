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
test = [2, 3, 6, 0, 4, 1, 5, 3]

def header():
  global test
  return LinkedList(head = linked(0))

def linked(i):
  global test
  if type(test[i]) is int:
    test[i] = Node(data = test[i], next = linked(test[i]))
  return
  

# node = LinkedList(Node(2, ))

def detect_twin(ls):
  pass

#print(detect_twin(test))

ll = header().head
while True:
  print(ll.data)
  ll = ll.next

  if ll == None:
    break