from algorithms import ALGORITHMS
import math
import pandas as pd
from time import time

bench = pd.read_csv('benchmark.csv')
if len(bench) > 0:
    run_id = int(max(bench['run_id']) + 1)
else:
    run_id = 0


semiprimes = open('semiprimes.txt')
for line in semiprimes:
    N, p, q = line.split(",")
    N = int(N)
    p = int(p)
    q = int(q)
    for alg in ALGORITHMS:
        if math.floor(math.log10(N)) > 17:
            if alg == "Trial division":
                continue
        if math.floor(math.log10(N)) > 50:
            if alg == "Pollard's rho" or alg=="Pollard's p-1":
                continue

        res = None
        if alg == "Quadratic sieve":
            if math.floor(math.log10(N)) <  35:
                L = math.exp(math.sqrt(math.log(N)*math.log(math.log(N))))
                B = int(math.pow(L,1/2+1/math.log10(N)))
                M = 10*B
            elif math.floor(math.log10(N)) < 51:
                B = 20000
                M = 80000
            else:
                B = 90000
                M = 80000
            start = time()
            res = ALGORITHMS[alg](N, B, M)
        elif alg == "Pollard's p-1":
            B = 10
            start = time()
            while res == None and B < math.sqrt(N):
                res = ALGORITHMS[alg](N,B=B)
                B *= 2
        elif alg == "Lenstra's elliptic curve":
            start = time()
            if math.floor(math.log10(N)) <  35:
                res = ALGORITHMS[alg](N)
            else:
                res = ALGORITHMS[alg](N,B1=1000000,B2=10000000)
        else:
            start = time()
            res = ALGORITHMS[alg](N)
        exec_time = time() - start

        if alg in ["Trial division", "Pollard's rho", "Pollard's p-1"]:
            if res == None:
                exec_time = "Failed"
        elif alg in ["Quadratic sieve", "Lenstra's elliptic curve"]:
            if res != set([p,q]):
                exec_time = "Failed"
            
        bench = pd.read_csv('benchmark.csv')
        if len(bench[(bench['algorithm']==alg)&(bench['N']==str(N))]['id']) > 0:
            id = max(bench[(bench['algorithm']==alg)&(bench['N']==str(N))]['id']) + 1
        else:
            id = 0
        
        with open('benchmark.csv','a') as file:
            file.write(f'{alg},{N},{p},{q},{exec_time},{id},{run_id}\n')
