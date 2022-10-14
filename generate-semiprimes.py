from sympy.ntheory.generate import randprime

interval_boundaries = [10**i for i in [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]]
amount_per_interval = 5

file = open('semiprimes.txt', 'a')
for i in range(len(interval_boundaries)-1):
    for j in range(amount_per_interval):
        p1 = randprime(interval_boundaries[i], interval_boundaries[i+1])
        p2 = randprime(interval_boundaries[i], interval_boundaries[i+1])
        file.write(str(p1*p2)+'\n')
