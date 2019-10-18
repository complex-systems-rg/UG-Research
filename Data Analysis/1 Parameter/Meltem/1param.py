from random import random
import numpy
import matplotlib.pyplot as plt

def f(x):
    return (x-2)*(x-10)*(x-16)

def error():
    return random()*500-250

def create_experiments(range1,range2, repet):
    datas = []

    for i in range(range1, range2):
        sum = 0
        for _ in range(repet):
            sum += f(i) + error()
        datas.append(round(sum/repet,2))
    return datas

experiment = create_experiments(0, 20, 100)

x = numpy.linspace(0, 20)
y = f(x)

plt.plot(x, y)
plt.plot(range(0,20), experiment)
plt.show()
