from heapq import heappush, heappop
import sys

G1 = {1:((2, 3), (3, 3)), 2:((3, 1), (4, 2)), 3:((4,50), ), 4:((2, 2), (3, 50), )}
G2 = {1:((2, 3), (3, 5)), 2:((3, 1), (4, 2)), 3:((4,50), ), 4:((2, 2), (3, 50), )}
G3 = {1:((2, 8), (3, 15)), 2:((1, 7), (3, 4), (4, 5)), 3:((1, 12), ), 4:((3, 5), )}
G4 = {1:((2, 8), (3, 17)), 2:((1, 7), (3, 10), (4, 5)), 3:((1, 12), ), 4:((3, 3), )}
G5 = {  1: ((2, 8), (3,10), (7,7)),
        2: ((1, 8), (3,3 ), (4,6)),
        3: ((7,11), (1,10), (2,3), (4,2), (5,1)),
        4: ((2, 6), (3,2 ), (5,1), (6,5)),
        5: ((3, 9), (6,4 ), (8,10)),
        6: ((5, 4), (4,5 ), (10,3)),
        7: ((1, 7), (3,11)),
        8: ((5,10), (9,1)),
        9: ((8, 1), ),
        10:((6, 3), (11,9), (12,2)),
        11:((10,9), (13,3)),
        12:((10,2), (13,1)),
        13:((12,1), (11,3))}

G6 = {}
with open('dijkstraData.txt', 'r') as f:
    for line in f.readlines():
        v = line.split('\t')[0]
        jws = line.split('\t')[1:-1]
        G6[int(v)] = [ tuple(map(int, jw.split(','))) for jw in jws ]

# return list contain distance of 1 to each nodes
def dijkstra(G):
    nodes_size = len(G)
    S = 1 # root node

    d = [2<<32 for i in range(nodes_size + 1)]
    d[S] = 0
    h = []
    heappush(h, (0, S))
    for i in range(nodes_size - 1):
        min_dist, k = 0, 0
        if not h: break
        while h:
            min_dist, k = heappop(h)
            if min_dist == d[k]: break

        for j, w in G[k]:
            if d[j] > d[k] + w:
                d[j] = d[k] + w
                heappush(h, (d[j], j))
    d.pop(0)
    return d

Gs = [G1, G2, G3, G4, G5, G6]
for G in Gs:
    print dijkstra(G)


