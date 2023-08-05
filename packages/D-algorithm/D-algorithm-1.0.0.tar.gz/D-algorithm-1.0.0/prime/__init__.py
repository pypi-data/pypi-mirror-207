P_List = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

def under_primes(n):
    num = []
    for i in range(1,10001):
        if prime(i) <= n:
            num.append(prime(i))
        else:
            return num

def prime(n):
    ls = primes(n)
    return ls[len(ls) - 1]

def primes(n):
    num = []
    nums = 1
    while len(num) < n:
        nums += 1
        if isprime(nums):
            num.append(nums)
    return num

def isprime(n):
    if n <= P_List[len(P_List) - 1]:
        if n in P_List:
            return True
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True