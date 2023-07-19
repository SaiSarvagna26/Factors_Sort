import math

def count_factors(n):
    count=0
    sqrt_n=int(math.sqrt(n))
    
    for i in range(1,sqrt_n + 1):
        if n %i==0:
            count+=1
            if i!=n//i:
                count+=1
    
    return count

def factors_sort(A):
    factor_counts = [(count_factors(num), num) for num in A]
    factor_counts.sort(key=lambda x: (x[0],x[1]))
    return [val for count,val in factor_counts]

A1 = list(map(int,input().split()))
print(factors_sort(A1)) 

