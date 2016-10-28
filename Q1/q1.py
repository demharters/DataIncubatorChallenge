#!/usr/bin/python

import numpy as np
import itertools

die = np.arange(1,7)

def myFunction(m,n):

    a = 0
    cter = 0
    products = []

    for diceInstance in itertools.product(die, repeat = m):
        if np.sum(diceInstance) == n:
            a=np.prod(diceInstance)
            products.append(a)
            #sys.stdout.write("Product: %.2f, Std: %.2f   \r" % (np.mean(products), np.std(products)))
            #sys.stdout.flush()
        else:
            pass
    
    return [np.mean(products), np.std(products)]

result1 = myFunction(8,24)
print "Product1: %.2f, Std1: %.2f" % (result1[0], result1[1])
#result2 = myFunction(50,150)
#print "Product2: %.2f, Std2: %.2f" % (result2[0], result2[1])
