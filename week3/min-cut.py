#  import graph_tool as gt
#  from graph_tool.all import *
import random
import copy
import time
import logging
import sys

#  logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
random.seed(int(time.time()))

def remove_duplicated_edge(A):
    B = copy.copy(A)
    for v in A:
        for adjacency in A[v]:
            if v in A[adjacency]: A[adjacency].remove(v)
                #  print "Remove (%d, %d)" % (adjacency, v)
    return A

#  ug = gt.Graph(directed=False)
A = {}

# prepare 200 vertices
#  vs = [ ug.add_vertex() for n in xrange(200) ]

#  f=sys.argv[1]
#  print f
with open('kargerMinCut.txt', 'r') as f:
#  with open(f, 'r') as f:
    for line in f.readlines():
        #  l = line.replace('\n', '').replace('\r', '').split('\t')
        l = line.replace('\n', '').replace('\r', '').split()
        v_node = int(l[0])
        A[v_node] = [ int(i) for i in l[1:] if i.isdigit() ]

# prepare 4 vertices
#  vs = [ ug.add_vertex() for n in xrange(4) ]

#  with open('exampleMinCut.txt', 'r') as f:
    #  for line in f.readlines():
        #  l = line.replace('\n', '').split('\t')
        #  v_node = int(l[0])
        #  A[v_node] = [ int(i) for i in l[1:] ]

vextice_len = len(A)

logging.debug('Orginaly: %s', str(A))
remove_duplicated_edge(A)
#  logging.debug('Remove Duplicate Edges: %s', str(A))

edges = []
for v, ad in A.items():
    [ edges.append((v, u)) for u in ad ]
edge_len = len(edges)

#  edges_shuffle = copy.copy(edges)
#  random.shuffle(edges_shuffle)

logging.debug('=' * 80)
loop = 0
while vextice_len > 2:
    loop += 1
    logging.debug('loop(%d): %s' % (loop, edges))

    #  1. figure out a edage by random
    edge_rm_id = random.randint(0, edge_len-1)

    logging.debug('remove: %s' % str(edges[edge_rm_id]))

    #  2. remove the edage
    rmd_edge = edges[edge_rm_id]
    for i in xrange(edges.count(rmd_edge)):
        edges.remove(rmd_edge)
        edge_len -= 1

    #  3. merge u to v
    logging.debug('merge u(%d) to v(%d)' % rmd_edge)
    new_edges = []
    o_u = random.choice((0, 1))
    o_v = 1 - o_u
    for i in xrange(len(edges)):
        u, v = edges[i]
        if u is rmd_edge[o_u]:
            edges[i] = (rmd_edge[o_v], v)
        elif v is rmd_edge[o_u]:
            edges[i] = (u, rmd_edge[o_v])

    vextice_len -= 1

    #  4. remove self-loop
    new_edges = []
    for i in xrange(len(edges)):
        u, v = edges[i]
        if not u is v: new_edges.append((u, v))
    edges = new_edges

    #  edges = list(set(edges))
    edge_len = len(edges)
    logging.debug('remove self-loop: %s' % str(edges))
    logging.debug('')

#  print edges
print('Min Cut: %d' % edge_len)
# draw
#  for edge in edges:
    #  ug.add_edge(vs[edge[0]-1], vs[edge[1]-1])

#  TODO: remove isolalting vertics
#  u, v = edges[0]
#  for i in xrange(len(vs)):
    #  if i is u-1: continue
    #  if i is v-1: continue
    #  ug.remove_vertex(vs[i])

#  graph_draw(ug, vertex_text=ug.vertex_index, vertex_font_size=10,
        #  output_size=(200, 200), output="/tmp/two-nodes.png")

