from pylab import *
import numpy as np
from math import pow, log
#  from numpy import arange, exp

def a(n):
    print np.power(n, 2) * np.log2(n)

def b(n):
    print np.power(2, n)

def c(n):
    print np.power(2, np.power(2, n))

def d(n):
    print np.power(n, np.log2(n))

def e(n):
    print np.power(n, 2)

#def draw():
#    n = np.arange(0.0, 100.00, 0.01)
#
#    a = np.power(n, 2) * np.log2(n)
#    b = np.power(2, n)
#    c = np.power(2, np.power(2, n))
#    d = np.power(n, np.log2(n))
#    e = np.power(n, 2)
#
#    #  s = sin(2*pi*t)
#    #  c = cos(2*pi*t)
#    plot(n, a, color = "blue")
#    #  plot(n, b, color = "red")
#    #  plot(n, c, color = "black")
#    #  plot(n, d, color = "pink")
#    plot(n, e, color = "green")
#
#    #  xlabel('time (s)')
#    #  ylabel('voltage (mV)')
#    #  title('About as simple as it gets, folks')
#    grid(True)
#    #  savefig("test.png")
#    show()

def main():
    #  draw()
    for i in xrange(5, 7):
        a(i)
        b(i)
        #  c(i)
        #  d(i)
        e(i)
        print

if __name__ == '__main__':
    main()
