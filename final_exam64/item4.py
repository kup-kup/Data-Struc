from random import randrange
import heapq, math

def mst(graph):
    heap = []
    tree = {}

    for u in graph:
        tree[u] = []

    u = list(graph)[0]
    for i in range(len(graph) - 1):
        for (w,v) in graph[u]:
            heapq.heappush(heap, (w, u, v))
        
        (w, u, v) = heapq.heappop(heap)
        while len(tree[v]) != 0:
            (w, u, v) = heapq.heappop(heap)
        
        tree[u].append((w, v))
        tree[v].append((w, u))
        u = v
    return tree

def shortest_path(graph, source, target):
    visited = {u: False for u in graph}
    distances = {u: math.inf for u in graph}
    paths = {u: None for u in graph}

    heap = []
    heapq.heappush(heap, (0, source))
    distances[source] = 0

    while heap:
        (distance_so_far, u) = heapq.heappop(heap)
        visited[u] = True

        for (w, v) in graph[u]:
            if not visited[v] and distance_so_far + w < distances[v]:
                distances[v] = distance_so_far + w
                paths[v] = (w, v)
                heapq.heappush(heap, (distances[v], v))
    
    result = {u: [] for u in graph}
    v = target
    while v != source:
        (w, v) = paths[v]
        result[u].append((w, v))
        v = u
    
    return result

graph = {
  0: [(3, 1), (1, 3), (4, 4)],
  1: [(3, 0), (5, 4), (4, 2)],
  2: [(4, 1), (1, 4), (2, 5)],
  3: [(1, 0), (6, 4)],
  4: [(4, 0), (5, 1), (1, 2), (6, 3), (3, 5)],
  5: [(2, 2), (3, 4)]
}

def solution(graph):
    num_node = len(graph)
    start = randrange(num_node)
    print(f"start: {start}")

    length = 0
    for node, list in graph.items():
        if node == start:
            continue
        
        print(f"shortest_path: {start} to {node}")
        print(shortest_path(graph, start, node))

#solution(graph)
#print(shortest_path(graph, 0, 1))

'''
shortest_path พัง
'''