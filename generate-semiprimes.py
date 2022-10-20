from sympy.ntheory.generate import randprime

interval_boundaries = [10**i for i in [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 27, 30, 33, 35]]
amount_per_interval = 1

file = open('semiprimes.txt', 'a')
for i in range(len(interval_boundaries)-1):
    for j in range(amount_per_interval):
        p = 0
        q = 0
        while p == q:
            p = randprime(interval_boundaries[i], interval_boundaries[i+1])
            q = randprime(interval_boundaries[i], interval_boundaries[i+1])
        file.write(f"{p*q},{p},{q}\n")
