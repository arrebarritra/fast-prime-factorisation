from algorithms import ALGORITHMS
import math
import pandas as pd
from time import time

bench = pd.read_csv('benchmark.csv')
if len(bench) > 0:
    run_id = int(max(bench['run_id']) + 1)
else:
    run_id = 0

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
        if len(bench[(bench['algorithm']==alg)&(bench['N']==str(N))]['id']) > 0:
            id = max(bench[(bench['algorithm']==alg)&(bench['N']==str(N))]['id']) + 1
        else:
            id = 0
        if len(bench) > 0:
            id = max(bench[(bench['algorithm']==alg)&(bench['N']==str(N))]['id']) + 1
        else:
            id = 0
        
        with open('benchmark.csv','a') as file:
            file.write(f'{alg},{N},{exec_time},{id},{run_id}\n')
