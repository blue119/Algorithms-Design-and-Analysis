import sys
import bisect

arr = []
with open('2sum.txt', 'r') as f:
    for line in f.readlines():
        arr.append(int(line))

# return min and max index of n + y between [-10000, 10000]
# a: array
# n: number
# i: low index
# j: high index
def bin_search(a, n, i, j):
    if i+1 == j : return j

    middle = (i + j) / 2;
    #  print a[middle]

    if (a[middle] + n) >= -10000:
        return bin_search(a, n, i, middle)
    else:
        return bin_search(a, n, middle, j)

def bin_search_min(a, n, i, j):
    if i+1 == j : return i

    middle = (i + j) / 2;
    #  print a[middle]

    if (a[middle] + n) <= 10000:
        return bin_search_min(a, n, middle, j)
    else:
        return bin_search_min(a, n, i, middle)

c = 0
d = 0
arr = sorted(arr)
#  arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]

#  i = bin_search(arr, arr[1], 0, len(arr))
#  j = bin_search_min(arr, arr[1], 0, len(arr))
#  print i, j

#  i = bin_search(arr, arr[2], 0, len(arr))
#  j = bin_search_min(arr, arr[2], 0, len(arr))
#  print i, j

#  i = bin_search(arr, arr[3], 0, len(arr))
#  j = bin_search_min(arr, arr[3], 0, len(arr))
#  print i, j

#  i = bin_search(arr, arr[0], 0, len(arr)-1)
#  j = bin_search_min(arr, arr[0], 0, len(arr)-1)
#  print i, j

#  -10000 - arr[1] <= j
#  10000 - arr[1]  >= j

i = arr[1]

result = []
for a in arr:
    min_j = -10000 - a
    max_j = 10000 - a

    #  max_index = bisect.bisect_left(arr, max_j)
    #  min_index = bisect.bisect_left(arr, min_j)
    #  if max_index > len(arr) - 1: max_index = len(arr) - 1

    max_index = bin_search(arr, a, 0, len(arr)-1)
    min_index = bin_search_min(arr, a, 0, len(arr)-1)
    min_index, max_index = sorted([min_index, max_index])
    if max_index > len(arr) - 1: max_index = len(arr) - 1


    for i in xrange(min_index, max_index+1):
        ret = arr[i] + a
        if ret <= 10000 and ret >= -10000: 
            c+=1
            if not ret in result: result.append(ret)
    #  if max_index != min_index+1:
        #  c+=1
        #  print arr[min_index-1] + a

print c
print len(result)



#  print max_j
#  print arr[-1]
#  print arr.index(99999663362)
#  print bisect.bisect_left(arr, min_j)
#  print bisect.bisect_left(arr, max_j)

#  print arr[bisect.bisect_left(arr, min_j)] + arr[1]
#  print arr[bisect.bisect_left(arr, max_j)]

sys.exit()

#  for k in xrange(12377, 12380):
#  for k in xrange(4, 5):
    #  print k
    #  i = bin_search_min(arr, arr[k], 0, len(arr))
    #  j = bin_search(arr, arr[k], 0, len(arr))
    #  print i, j
    #  print arr[i]
    #  print arr[j]
    #  print arr[i] + arr[k]
    #  print arr[j] + arr[k]


result = []
for a in arr:
    max_index = bin_search(arr, a, 0, len(arr)-1)
    min_index = bin_search_min(arr, a, 0, len(arr)-1)
    min_index, max_index = sorted([min_index, max_index])

    for i in xrange(min_index, max_index+1):
        ret = arr[i] + a
        if ret <= 10000 and ret >= -10000: c+=1
        if not ret in result: result.append(ret)
    #  if max_index != min_index+1:
        #  c+=1
        #  print arr[min_index-1] + a
        #  print arr[min_index] + a
        #  print arr[min_index+2] + a
        #  print max_index, min_index
    #  if max_index > (min_index+1):
        #  c+=1
        #  if (max_index - min_index) > d: d = (max_index - min_index)

print len(result)

#  print arr.index(-99999653362)
#  print arr.index(-99999376014)
#  k = arr[12345]

#  for a in arr[12345:21214]:
    #  bbb = []
    #  for b in arr:
        #  if a + b <= 10000 and a + b >= -10000:
            #  bbb.append(a+b)
    #  if bbb:
        #  print a, arr.index(a), bbb


#  print
#  print i
#  print j
#  print
#  print arr[0]
#  print arr[200000]
#  print arr[i]
#  print arr[200000] + arr[j-1]
#  print arr[200000] + arr[j]
#  print arr[200000] + arr[j+1]
#  print arr[i]
#  print arr[0]
#  print arr[1]
sys.exit()

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


