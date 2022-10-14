from algorithms import ALGORITHMS
import numpy as np
import pandas as pd
from time import time

for alg in ALGORITHMS:
    semiprimes = open('semiprimes.txt')
    for N in semiprimes:
        N = int(N)
        start = time()
        if alg == "Quadratic sieve":
            L = np.exp(np.sqrt(np.log(N)*np.log(np.log(N))))
            B = int(np.power(L,np.sqrt(2)/4))
            M = int(np.power(L,3*np.sqrt(2)/4))
            ALGORITHMS[alg](N, B, M)
        else:
            ALGORITHMS[alg](N)
        exec_time = time() - start
        bench = pd.read_csv('benchmark.csv')
        id = len(bench[(bench['algorithm']==alg)&(bench['N']==N)])
        with open('benchmark.csv','a') as file:
            file.write(f'{alg},{N},{exec_time},{id}\n')
