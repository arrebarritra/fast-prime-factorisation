from algorithms import ALGORITHMS
import math
import pandas as pd
from time import time


for alg in ALGORITHMS:
    semiprimes = open('semiprimes.txt')
    for N in semiprimes:
        if len(N) > 15:
            if alg == "Trial division":
                continue
        N = int(N)
        start = time()
        if alg == "Quadratic sieve":
            L = math.exp(math.sqrt(math.log(N)*math.log(math.log(N))))
            B = int(math.pow(L,math.sqrt(2)/4))
            M = int(math.pow(L,3*math.sqrt(2)/4))
            ALGORITHMS[alg](N, B, M)
        else:
            ALGORITHMS[alg](N)
        exec_time = time() - start
        bench = pd.read_csv('benchmark.csv')
        id = len(bench[(bench['algorithm']==alg)&(bench['N']==N)])
        with open('benchmark.csv','a') as file:
            file.write(f'{alg},{N},{exec_time},{id}\n')
