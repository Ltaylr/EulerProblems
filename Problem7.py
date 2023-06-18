import numpy as np

#naive sieve of erasthamus implementation
length = 10**6
nthPrime = 10001
arr = np.array([True]*length, dtype=bool)

i = 1

arr[0] = False

count = 0;



while i < len(arr) and count < nthPrime:
    cur = i
    #find next prime
    while i < len(arr) and arr[i] == False:
        i+=1
    #increment prime count
    count+=1
    #set x to current i
    x = i
    step = i+1
    #iterate over list set multiples to fasle (not prime)
    while x < len(arr)-step:
        #i is offset by 1, add i+1
        x+=step
        arr[x] = False
    i+=1
    
print(count, "-th prime:", i)
