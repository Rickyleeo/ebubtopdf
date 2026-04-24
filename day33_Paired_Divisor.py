import math

def get_sum_of_divisors(n):
    if n < 2: return 0
    s = 1  # 1 is always a divisor
    # Optimization: Only iterate up to the square root of n
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            s += i
            # If divisors are not the same (e.g., not 6*6=36), add the paired divisor
            if i*i != n: 
                s += n // i
    return s

if __name__ == "__main__":
    limit = 3000
    print(f"All amicable numbers within {limit}:")
    
    # Dictionary to cache calculated sums to avoid redundant computations
    sums = {} 
    
    for a in range(1, limit):
        # Calculate sum of divisors for 'a' if not already in cache
        if a not in sums:
            sums[a] = get_sum_of_divisors(a)
        
        b = sums[a]
        
        # Amicable pair definition: sum(a)==b, sum(b)==a, and a != b
        # 'a < b' ensures each pair is printed only once
        if a < b:
            if b not in sums:
                sums[b] = get_sum_of_divisors(b)
            if sums[b] == a:
                print("%4d -- %4d" % (a, b))
