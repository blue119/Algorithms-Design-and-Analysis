import heapq

class HEAPQ(object):
    # default extract is min
    def __init__(self, key = lambda x, y: x < y):
        ''' the default sorting key is for extract_min
        '''
        assert hasattr(key, '__call__')
        self.cmpfn = key
        self.array_len = 0
        self.array = [0] # don't use first slot

    def _swap(self, n1, n2):
        self.array[n1], self.array[n2] = self.array[n2], self.array[n1]

    def heapify(self, arr):
        for v in arr:
            self.push(v)
        return self.dump()

    def bubble_up(self, cur):
        if cur == 1: return

        p = cur / 2 # parent
        if self.cmpfn(self.array[cur], self.array[p]):
            self._swap(cur, p)
            self.bubble_up(p)

    def push(self, v):
        self.array.append(v)
        self.array_len += 1
        if self.array_len > 1:
            self.bubble_up(self.array_len)

    def bubble_down(self, cur):
        l = cur * 2       # left(i)
        r = (cur * 2) + 1 # right(i)

        n = cur # next node
        #  print n, l, r, self.array_len
        if l <= self.array_len and self.cmpfn(self.array[l], self.array[cur]):
            n = l

        if r <= self.array_len and self.cmpfn(self.array[r], self.array[n]): # swap to max node
            n = r

        if cur != n: # shift down
            self._swap(cur, n)
            self.bubble_down(n)

    def pop(self):
        self._swap(1, -1)
        self.array_len -= 1
        r = self.array.pop()
        self.bubble_down(1)
        return r

    def dump(self):
        return self.array[1:]

def verify(array):
    import copy

    a = copy.deepcopy(array)
    heapq.heapify(a)
    print array
    print a
    if array == a:
        print "Equal"
    else:
        print "Not Equal"

def main():
    # we shall consider the list from element 1, not 0
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    #  key = lambda x, y: x > y #extract_max
    #  hq = HEAPQ(key = key)
    hq = HEAPQ()
    hq.heapify(arr)
    verify(hq.dump())

    arr = [('aa', 16), ('bb', 4), ('cc', 10), ('dd', 14), ('ee', 7),
            ('ff', 9), ('gg', 3), ('hh', 2), ('ii', 8), ('jj', 1)]

    key = lambda x, y: x[1] < y[1] #extract_max
    hq = HEAPQ(key = key)
    hq.heapify(arr)
    print hq.dump()

if __name__ == "__main__":
    main()


