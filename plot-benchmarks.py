import matplotlib.pyplot as plt
import pandas as pd
from algorithms import ALGORITHMS

bench = pd.read_csv('benchmark.csv')
for alg in ALGORITHMS:
    x = bench[bench['algorithm']==alg]['N']
    y = bench[bench['algorithm']==alg]['time']
    plt.semilogx(x, y, label=alg)
plt.legend()
plt.show()