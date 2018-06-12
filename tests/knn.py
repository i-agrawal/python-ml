#!/bin/python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import mlimpl as ml

if __name__ == "__main__":
    # load data
    data = np.loadtxt(open("data/iris.data", "rb"), delimiter=",")
    x = data[:, :data.shape[1]-1]
    y = data[:, data.shape[1]-1].astype(int)

    # find the best k
    best = 0
    for k in range(1,10):
        pred = ml.knn(x,y,k)
        accuracy = np.sum(pred == y) / x.shape[0]
        print("k = %d, accuracy = %f" % (k,accuracy))
        if best < accuracy:
            bk = k
            best = accuracy

    # display slice with best k
    pred = ml.knn(x,y,bk)
    ind = np.where(pred==0)
    plt.scatter(x[ind, 0], x[ind, 1])
    ind = np.where(pred==1)
    plt.scatter(x[ind, 0], x[ind, 1])
    ind = np.where(pred==2)
    plt.scatter(x[ind, 0], x[ind, 1])
    plt.show()