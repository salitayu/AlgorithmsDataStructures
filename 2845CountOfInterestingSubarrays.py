def countInterestingSubarrays(nums, modulo):
    n = len(nums)
    cnt = Counter([0])
    res = 0
    prefix = 0
    for i in range(n):
        prefix += 1 if nums[i] % modulo == k else 0
        res += cnt[(prefix - k + modulo) % modulo]
        cnt[prefix % modulo] += 1
    return res
    # time O(n)
    # space O(min(n, modulo))