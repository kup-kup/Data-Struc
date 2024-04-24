from math import cos, asin, sqrt, pi
import heapq

def distance(latlon1, latlon2):
    (lat1, lon1) = latlon1
    (lat2, lon2) = latlon2
    p = pi / 180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

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

provinces = {
    "Bangkok": (13.754, 100.501),
    "Samut Prakan": (13.599, 100.597),
    "Nonthaburi": (13.861, 100.515),
    "Udon Thani": (17.416, 102.786),
    "Chon Buri": (13.362, 100.983),
    "Nakhon Ratchasima": (14.971, 102.102),
    "Chiang Mai": (18.79, 98.985),
    "Sgonkhla": (7.008, 100.477),
    "lampang": (18.292, 99.493),
    "Phuket": (7.879, 98.398)
}

graph = {p:[] for p in provinces}

for p1 in provinces:
    for p2 in provinces:
        if p1 == p2:
            continue
        dis = round(distance(provinces[p1], provinces[p2]))
        graph[p1].append((dis, p2))

mst_graph = mst(graph)

# for key, value in mst_graph.items():
#     print(key, len(value))
#     count += len(value)
#     for i in value:
#         print(f"   {i}")
