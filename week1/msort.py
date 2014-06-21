import random
import logging

#  logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def merge_count_split_inverstions(l, r, mid):
    i = 0
    j = 0
    inv = 0
    result = []

    logging.debug('l: %s, r: %s' % (str(l), str(r)))
    while i < len(l) and j < len(r):
            if l[i] > r[j]:
                result.append(r[j])
                inv+=(mid-i)
                j += 1
            else:
                result.append(l[i])
                i += 1
    result += l[i:]
    result += r[j:]
    return (result, inv)

def msort_count_split_inversions(x, mid):
    logging.debug('msort(%s, %s)' % (str(x), mid))

    if len(x) == 1:
        return (x, 0)

    mid = int(len(x)/2)
    l, l_inv = msort_count_split_inversions(x[:mid], mid)
    r, r_inv = msort_count_split_inversions(x[mid:], mid)
    z, z_inv = merge_count_split_inverstions(l, r, mid)

    logging.debug('result: %s, inv %d' % (str(z), l_inv + r_inv + z_inv))
    return (z, l_inv + r_inv + z_inv)

def main():
    """@todo: Docstring for main.

    :arg1: @todo
    :returns: @todo

    """
    unsorted = []
    unsorted = [6,5,4,3,2,1]
    mid = len(unsorted)/2
    (has_sorted, c) = msort_count_split_inversions(unsorted, mid)
    print (has_sorted, c)

    unsorted = [2,4,6,1,3,5]
    mid = len(unsorted)/2
    (has_sorted, c) = msort_count_split_inversions(unsorted, mid)
    print (has_sorted, c)

    unsorted = random.sample(xrange(100), 6)
    mid = len(unsorted)/2
    (has_sorted, c) = msort_count_split_inversions(unsorted, mid)
    print (has_sorted, c)

    unsorted = []
    with open('IntegerArray.txt', 'r') as f:
        for i in f.readlines():
            unsorted.append(int(i))

    mid = len(unsorted)/2
    (has_sorted, c) = msort_count_split_inversions(unsorted, mid)
    #  print (has_sorted, c)
    print (c)

if __name__ == '__main__':
    main()

