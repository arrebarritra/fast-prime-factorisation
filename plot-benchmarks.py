import matplotlib.pyplot as plt
import pandas as pd
from algorithms import ALGORITHMS

plt.rc('text', usetex=True)

bench = pd.read_csv('benchmark.csv')
bench = bench[(bench['run_id']>=20)&(bench['time']!='Failed')]
for alg in ALGORITHMS:
    x = bench[bench['algorithm']==alg]['N'].to_numpy()
    xint = []
    for el in x:
        xint += [int(el)]
    y = pd.to_numeric(bench[bench['algorithm']==alg]['time'])
    plt.loglog(xint, y, marker='o', label=alg)

plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.legend()

plt.show()