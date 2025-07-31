nums = [82,217,170,215,153,55,185,55,185,232,69,131,130,102]

def rob_rec(nums):
    return rob_rec_helper(nums, 0)

def rob_rec_helper(nums, start):
    n = len(nums)
    if start >= n:
        return 0
    if start == n - 1:
        return nums[start]
    if start == n - 2:
        if nums[start] > nums[start + 1]:
            return nums[start]
        else:
            return nums[start + 1]
    if start == n - 3:
        return nums[start] + nums[start + 2]
    
    res1 = nums[start + 0] + rob_rec_helper(nums, start + 2)
    res2 = nums[start + 0] + rob_rec_helper(nums, start + 3)
    res3 = nums[start + 1] + rob_rec_helper(nums, start + 3)
    res4 = nums[start + 1] + rob_rec_helper(nums, start + 4)

    print(start, res1, res2, res3, res4)

    return max([res1, res2, res3, res4])

def rob_dp(nums):
    return rob_dp_helper(nums, 0, {})

def rob_dp_helper(nums, start, memo):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max([nums[0], nums[1]])
    if n == 3:
        return max([nums[1], nums[0] + nums[2]])
    if n >= 4:
        if start >= n:
            return 0
        if start == n - 1:
            return nums[start]
        if start == n - 2:
            return max([nums[start], nums[start + 1]])
        if start == n - 3:
            return max([nums[start + 1], nums[start] + nums[start + 2]])
        
        if (start + 2) in memo is not None:
            return memo[start + 2]
        if (start + 3) in memo is not None:
            return memo[start + 3]
        if (start + 4) in memo is not None:
            return memo[start + 4]
        
        dp2 = rob_dp_helper(nums, start + 2, memo)
        dp3 = rob_dp_helper(nums, start + 3, memo)
        dp4 = rob_dp_helper(nums, start + 4, memo)

        res1 = nums[start + 0] + dp2
        res2 = nums[start + 0] + dp3
        res3 = nums[start + 1] + dp3
        res4 = nums[start + 1] + dp4

        memo[start + 2] = dp2
        memo[start + 3] = dp3
        memo[start + 4] = dp4

        return max([res1, res2, res3, res4])


print(rob_rec(nums))
print(rob_dp(nums))