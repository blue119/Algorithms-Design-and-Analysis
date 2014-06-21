import random
import logging
from copy import copy

#  logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

comparisons = 0

def swap(a, n1, n2):
    """@todo: Docstring for swap.

    :a: @todo
    :n1: @todo
    :n2: @todo
    :returns: @todo

    """
    a[n1], a[n2] = a[n2], a[n1]

def qsort_choosePivot(A):
    return 0

def qsort_partition(A, l, r, pivot):

    global comparisons
    comparisons += (r-l)

    p = A[pivot]
    if not pivot is l: swap(A, l, pivot)

    i = l + 1
    for j in xrange(l+1, r+1):
        if A[j] < p:
            swap(A, i, j)
            i += 1

    swap(A, i-1, l)

    return (i-1)


def qsort_l(A, l, r):
    if l >= r: return

    pivot = qsort_partition(A, l, r, l)
    qsort_l(A, l, pivot-1)
    qsort_l(A, pivot+1, r)

    return A

def qsort_r(A, l, r):
    if l >= r: return

    pivot = qsort_partition(A, l, r, r)
    qsort_r(A, l, pivot-1)
    qsort_r(A, pivot+1, r)

    return A

def look_for_m(A, l, r, m):
    lv = A[l]
    mv = A[m]
    rv = A[r]

    if (lv > mv and lv < rv) or (lv < mv and lv > rv): return l
    if (mv > lv and mv < rv) or (mv < lv and mv > rv): return m
    if (rv > lv and rv < mv) or (rv < lv and rv > mv): return r
    return r

def qsort_m(A, l, r):
    if l >= r: return

    m = look_for_m(A, l, r, (l+r)/2)
    pivot = qsort_partition(A, l, r, m)
    qsort_m(A, l, pivot-1)
    qsort_m(A, pivot+1, r)

    return A

def main():
    global comparisons
    unsorted = []

    quick_fn = [qsort_l, qsort_r, qsort_m]
    for fn in quick_fn:
        comparisons = 0
        unsorted = [3, 8, 2, 5, 1, 4, 7, 6]
        has_sorted = copy(unsorted)
        has_sorted = fn(has_sorted, 0, len(unsorted)-1)
        if not has_sorted == sorted(unsorted): print '%s fail: %s' % (fn.func_name, has_sorted)
        print fn.func_name, 'comparisons:', comparisons


    #  for i in xrange(10000):
        #  unsorted = random.sample(xrange(100000), 1000)
        #  pivot = 0
        #  try:
            #  has_sorted = qsort_m(unsorted, pivot, len(unsorted)-1)
            #  if not has_sorted == sorted(unsorted):
                #  print unsorted
                #  print has_sorted
                #  break
        #  except:
            #  print 'except'
            #  print unsorted
            #  break

    unsorted = []
    with open('QuickSort.txt', 'r') as f:
        for i in f.readlines():
            unsorted.append(int(i))

    for fn in quick_fn:
        comparisons = 0
        has_sorted = copy(unsorted)
        has_sorted = fn(has_sorted, 0, len(unsorted)-1)
        if not has_sorted == sorted(unsorted): print '%s fail: %s' % (fn.func_name, has_sorted)
        print fn.func_name, 'comparisons:', comparisons

if __name__ == '__main__':
    main()

