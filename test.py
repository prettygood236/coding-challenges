def prime_list(num):
    sieve = [True] * (num+1)
    m = int(num**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i*2,num+1,i):
                sieve[j] = False
    return [i for i,v in enumerate(sieve,start=2) if v==True]

print(prime_list(17))
