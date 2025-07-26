def fibonacci_dp(n, memo):
    if n == 0 or n == 1:
        return n
    
    if n in memo is not None:
        return memo[n]
    
    res = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    memo = res
    return res

def tribonacci_dp(n, memo):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    
    if n in memo is not None:
        return memo[n]

    res = tribonacci_dp(n - 1, memo) + tribonacci_dp(n - 2, memo) + tribonacci_dp(n - 3, memo)
    memo[n] = res
    return res

print(fibonacci_dp(10, {}))
print(tribonacci_dp(10, {}))