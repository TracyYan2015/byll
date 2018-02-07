# -*- coding:utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
plt.xlabel('dose')
plt.ylabel('delta of V')

w = [0]
dt = 1.0
a_mu = 570.8 * 8
a_sigma = 6.7471 * 100


# standard brownian motion
def _sbm(t, dt):
    N = int(math.ceil(float(t)/dt))
    w = [0] * N
    dw = [0] * N
    dw[0] = math.sqrt(dt)*random.gauss(0,1)
    for i in range(1, N):
        dw[i] = math.sqrt(dt)*random.gauss(0,1)
        w[i] = dw[i] + w[i-1]
    # d = dict()
    # for i,v in enumerate(w):
    #     d[i+1] = v
    # return d
    return w[N-1]


# standard Brownian motion
def sbm(t, dts):
    if isinstance(dts, list):
        for dt in dts:
            x,y = _sbm(t, dt)


# dose: dose
# bm: brownian motion of dose
def deltaV(dose, bm):
    a = random.gauss(a_mu, a_sigma)
    b = a * 0.01731 * math.exp(0.01731 * dose)
    c = 8.1854e-1 * bm
    # print 'b: %f, c: %f' % (b,c)
    return b + c


# 画出阈值电压的漂移值随着总剂量效应剂量之间的关系图
def showDoseDeltaV():
    dose = 100
    doses = range(1, dose)
    d_dose = 1.0
    N = dose - 1
    deltaVs = []
    for dose in doses:
        deltaVs.append(deltaV(dose, _sbm(dose, d_dose)))
    plt.plot(doses, deltaVs)
    plt.show()


#画出不同剂量下的失效概率
def showDoseFailProb():
    failThreshold = 200.0
    dose = 100
    doses = range(1, dose)
    d_dose = 1.0
    N = dose - 1
    probs = []
    for dose in doses:
        print failThreshold/(0.01731 * math.exp(0.01731 * dose))
        probs.append(1.0 - stats.norm.cdf(failThreshold/(0.01731 * math.exp(0.01731 * dose)), a_mu, a_sigma))
    # print 'probs: %s' % str(probs)
    plt.plot(doses, probs)
    plt.show()


def main():
    showDoseDeltaV()
    showDoseFailProb()

if __name__ == '__main__':
    main()