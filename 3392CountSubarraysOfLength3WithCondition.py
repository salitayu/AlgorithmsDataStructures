def countSubarrays(nums):
    n = len(nums)
    ans = 0
    for i in range(1, n - 1):
        if nums[i] == (nums[i-1] + nums[i+1]) * 2:
            ans += 1
    return ans
    # time o(n)
    # space o(1)