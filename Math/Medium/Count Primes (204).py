class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        isPrime = [True for i in range(n+1)]
        for i in range(2,n):
            if isPrime[i]:
                count+=1
            for j in range(i * i,n,i):
                isPrime[j] = False
        return count
    
                
                