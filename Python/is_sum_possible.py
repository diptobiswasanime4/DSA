# find out is sum possible?

sum = 30
nums = [4, 6, 10]

def is_sum_possible_rec(sum, nums):
    if sum == 0:
        return True
    if sum < 0:
        return False
    for num in nums:
        res = is_sum_possible_rec(sum - num, nums)
        # print("res:", res)
        if res == True:
            return True
    return False

def is_sum_possible_dp(sum, nums, memo):
    if sum == 0:
        return True
    if sum < 0:
        return False
    if sum in memo is not None:
        return memo[sum]
    for num in nums:
        res = is_sum_possible_dp(sum - num, nums, memo)
        memo[sum - num] = res
        # print("res:", res)
        if res == True:
            return True
    return False

print(is_sum_possible_rec(sum, nums))
print(is_sum_possible_dp(sum, nums, {}))