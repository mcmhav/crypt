from math import exp

def gcd(a,b):
    while a:
            a, b = b%a, a
    return b
       
def witness(n):
    a = 1
    cou = 0
    nw = 0
    while a <= n:
        g = gcd(a, n)
        if g == 1:
            t = (pow(a,(n-1)))%n
            #if t == 1:
                #print ' ', a, g, t
            cou = cou + 1
        else:
            print a, g
            nw = nw + 1
        a = a + 1
    print cou
    print nw

witness(323)