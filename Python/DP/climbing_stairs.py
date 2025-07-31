# In how many distinct ways you can climb n stairs taking either 1 or 2 steps.

def climb_rec(n):
    if n <= 0:
        return 1
    return climb_rec(n - 1) + climb_rec(n - 2)

def climb_dp(n, memo):
    if n <= 0:
        return 1
    if n in memo is not None:
        return memo[n]
    res = climb_dp(n - 1, memo) + climb_dp(n - 2, memo)
    memo[n] = res
    return res

print(climb_rec(2))
print(climb_rec(3))
print(climb_rec(4))
print(climb_rec(10))

print(climb_dp(2, {}))
print(climb_dp(3, {}))
print(climb_dp(4, {}))
print(climb_dp(10, {}))