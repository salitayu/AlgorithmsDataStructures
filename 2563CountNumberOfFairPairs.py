def lower_bound(nums, low, high, element):
    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] >= element:
            high = mid - 1
        else:
            low = mid + 1
    return low
def countFairPairs(nums, lower, upper):
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        low = lower_bound(nums, i + 1, len(nums) - 1, lower - nums[i])
        high = lower_bound(nums, i + 1, len(nums) - 1, upper - nums[i] + 1)
        ans += high - low
    return ans
# time complexity: o(nlogn)
# space complexity: o(n) or o(logn)