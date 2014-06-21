import random
import numpy as np
import matplotlib.pyplot as plt
import time

def rand_point(rng, num):
    """@todo: Docstring for rand_point.
    :returns: @todo

    """
    x = random.sample(xrange(rng), num)
    y = random.sample(xrange(rng), num)
    #  return zip(x, y)
    return (x, y)

def dst_len(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = np.power(x1 - x2, 2)
    y = np.power(y1 - y2, 2)
    return np.sqrt(x+y)

def brute_force(xy):
    m = 1<<32
    xy_m = ()
    c = 0

    for p1 in xy:
        c+=1
        for p2 in xy[c:]:
            if p1 is p2: continue
            dst = dst_len(p1, p2)
            if dst < m:
                m = dst
                xy_m = (p1, p2)

    return (m, xy_m)

def closestpair(L):
    # Work around ridiculous Python inability to change variables in outer scopes
    # by storing a list "best", where best[0] = smallest sqdist found so far and
    # best[1] = pair of points giving that value of sqdist.  Then best itself is never
    # changed, but its elements best[0] and best[1] can be.
    #
    # We use the pair L[0],L[1] as our initial guess at a small distance.
    best = [dst_len(L[0],L[1]), (L[0],L[1])]

    # check whether pair (p,q) forms a closer pair than one seen already
    def testpair(p,q):
        d = dst_len(p,q)
        if d < best[0]:
            best[0] = d
            best[1] = p,q

    # merge two sorted lists by y-coordinate
    def merge(A,B):
        i = 0
        j = 0
        while i < len(A) or j < len(B):
            if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
                yield A[i]
                i += 1
            else:
                yield B[j]
                j += 1

    # Find closest pair recursively; returns all points sorted by y coordinate
    def recur(L):
        #  print '1', L
        if len(L) < 2: return L

        split = len(L)/2
        splitx = L[split][0]
        L = list(merge(recur(L[:split]), recur(L[split:])))
        #  print '2', L, splitx

        # Find possible closest pair across split line
        # Note: this is not quite the same as the algorithm described in class, because
        # we use the global minimum distance found so far (best[0]), instead of
        # the best distance found within the recursive calls made by this call to recur().
        # This change reduces the size of E, speeding up the algorithm a little.
        #
        E = [p for p in L if abs(p[0] - splitx) < best[0]]
        for i in range(len(E)):
            for j in range(1,8):
                if i+j < len(E):
                    testpair(E[i], E[i+j])
        #  print best
        return L

    print 
    recur(L)
    return best

def main():
    xs, ys = rand_point(1000000, 2000)
    xy = zip(xs, ys)
    xy.sort()
    #  xy = [(10, 49), (21, 2), (28, 6), (38, 35), (41, 17), (50, 13), (63, 25), (76, 53), (86, 9), (91, 54)]
    #  print xy

    t1 = time.time()
    m, xy_m = closestpair(xy)
    print 
    print "Closest Pair"
    print "min dst: ", m, str(xy_m)
    print "elapse: ", time.time() - t1
    x_m, y_m = zip(xy_m[0], xy_m[1])
    print 

    t1 = time.time()
    m, xy_m = brute_force(xy)
    print "Brute Force"
    print "min dst: ", m, str(xy_m)
    print "elapse: ", time.time() - t1


    # evenly sampled time at 200ms intervals
    #  t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    #  plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    #  plt.plot(xy)

    #  plt.plot(xs, ys, 'ro')
    #  plt.plot(x_m, y_m)
    # You can specify a rotation for the tick labels in degrees or with keywords.
    #  plt.xticks(x, labels, rotation='vertical')
    # Pad margins so that markers don't get clipped by the axes
    #  plt.margins(0.2)
    # Tweak spacing to prevent clipping of tick-labels
    #  plt.subplots_adjust(bottom=0.15)

    #  plt.show()

if __name__ == '__main__':
    main()
