#! /usr/bin/python3

import random
import math
import sys

random.seed(14649)

def rabinMiller(n):
     s = n-1
     t = 0
     while s&1 == 0:
         s = s//2
         t +=1
     k = 0
     while k<64:
         a = random.randrange(2,n-1)
         #a^s is computationally infeasible.  we need a more intelligent approach
         #v = (a**s)%n
         #python's core math module can do modular exponentiation
         v = pow(a,s,n) #where values are (num,exp,mod)
         if v != 1:
             i=0
             while v != (n-1):
                 if i == t-1:
                     return False
                 else:
                     i = i+1
                     v = (v**2)%n
         k+=1
     return True

def isPrime(n):
     #lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
     #under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
     #of composite numbers from our potential pool without resorting to Rabin-Miller
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     #k is the desired bit length
     r=100*(math.log(k,2)+1) #number of attempts max
     r_ = r
     while True:
        #randrange is mersenne twister and is completely deterministic
        #unusable for serious crypto purposes
         n = random.randrange(2**(k-1),2**(k))
         r-=1
         if isPrime(n) == True:
             return n

def bti(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

gcd = lambda m,n: m if not n else gcd(n,m%n)

plaintext = "crossctf{RSA_Challenges_Are_Too_Easy} Well I'm supposed to pad this bit with some stuff, but I'm not too sure what to put here, so therefore you'll get something from the RSA wikipedia page."

plain = plaintext.encode()
m = bti(plain)
#### ^ Helpers ^ ####

def bestow(c, e):
    print ("c = " + str(c))
    print ("e = " + str(e))
    print (" ")

def give():
    p = generateLargePrime(size)
    q = generateLargePrime(size)
    phin = (p-1)*(q-1)
    n = p*q
    e = 1
    for i in primes:
        if phin%i == 0:
            return give()
    return (p, q, n)

size = 4096 #Change this number to set number of bits
primes = [7283, 1873, 2357, 1999, 5749]

print (m)
'''
output = give()
print ("n = " + str(output[-1]))
print (" ")

def givee(skip):
    e = 1
    for i in range(5):
        if i == skip:
            continue
        e *= primes[i]
    return e

for i in range(5):
    e = givee(i)
    c = pow(m, e, output[-1])
    bestow (c, e)
'''
