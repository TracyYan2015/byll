#-*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

a_mu = 0.1754
a_sigma = math.sqrt(5.3779e-4)
# a = random.gauss(a_mu, a_sigma)
# when a is not 'good', uncomment this. 
a = 0.135772795631
b = 12.0
fail_threshold = 0.7

def Pmax(dose):
    # print 'a: %f' % a
    return 1 - a * math.log(1 + float(dose) * b)


def showDosePmax():
    # doses = map(lambda x: math.pow(10, x), range(1, 7))
    doses = map(lambda x: x/100.0, range(1, 51))
    print 'doses: %s' % str(doses)
    powers = map(Pmax, doses)
    print 'p: %s' % str(powers)
    plt.xlabel('dose(rad)')
    plt.ylabel('normalized Pmax(V)')
    plt.plot(doses, powers)
    plt.show()


def showDoseFailProb():
    # compute 1-a*log(1+D*28) < 0.8
    # e.g. a*log(1+D/...) > 0.2 
    # e.g. a > 0.2/log(1+D/...) 
    doses = map(lambda x: x / 100.0, range(1, 51))
    def f(a_mu, a_sigma):
        def g(x):
            return 1 - stats.norm.cdf(x, a_mu, a_sigma)
        return g
    h = f(a_mu, a_sigma)
    print "x: %s" % str(map(lambda dose: (1 - fail_threshold)/math.log(1+float(dose)*b), doses))
    probs = map(h, map(lambda dose: (1 - fail_threshold)/math.log(1+float(dose)*b), doses))
    doses_x = []
    for dose in doses:
        doses_x.append(math.log(dose, 10))
    plt.xlabel('dose(rad)')
    plt.ylabel('failure probability')
    plt.plot(doses, probs)
    plt.show()


def main():
    print 'a: %s' % str(a)
    # showDosePmax()
    showDoseFailProb()


if __name__ == '__main__':
    main()




