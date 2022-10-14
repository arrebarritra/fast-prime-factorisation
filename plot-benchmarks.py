import matplotlib.pyplot as plt
import pandas as pd
from algorithms import ALGORITHMS

bench = pd.read_csv('benchmark.csv')
for alg in ALGORITHMS:
    x = bench[bench['algorithm']==alg]['N'].to_numpy()
    xint = []
    for el in x:
        xint += [int(el)]
    y = bench[bench['algorithm']==alg]['time']
    plt.semilogx(xint, y, marker='o', linestyle='None', label=alg)
plt.legend()
plt.show()