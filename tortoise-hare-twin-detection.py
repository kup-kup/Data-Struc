test = [2, 3, 6, 0, 4, 1, 5, 3]

def detect_twin(ls):
  i = ls[0]
  j = ls[ls[0]]

  while i != j:
    if i >= len(ls) or j >= len(ls): 
      return False
    print(i, j)
    i = ls[i]
    j = ls[ls[i]]
    
  return True

print(detect_twin(test))