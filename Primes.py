#Nicolas Tracewell
#ntracewe@ucsc.edu
#programming assignment 4
#The program lists consecutive primes. It will list the same number of primes as the number that is input by the user.

def isPrime(m, L):
    sqrt = int(m**(1/2))
    isPrime = True
    for i in range(0 , len(PrimeList)):
        if sqrt < PrimeList[i]:
            break
        if m%PrimeList[i] == 0:
            isPrime = False
        if isPrime == False:
            break
    if isPrime == True:
        PrimeList.append(m)

n = int(input("Enter the number of Primes to compute: "))
PrimeList = [2]
L = PrimeList
m = 3

while len(PrimeList)<n+1:
    isPrime(m, L)
    m+=1
for j in range (0, n):
    print(PrimeList[j], " ", end="")
    if j>0 and (j+1)%10 == 0:
        print("\n")