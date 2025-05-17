def countCompleteSubarrays(nums):
    result = 0
    window_count = collections.defaultdict(int)
    total_distinct_count = len(set(nums))
    left = 0
    for right in range(len(nums)):
        window_count[nums[right]] += 1
        if len(window_count) < total_distinct_count:
            continue
        while left <= right and len(window_count) == total_distinct_count:
            # here we know that [left, right] is a valid window
            # therefore, count the subarray itself and all the existing ones extending it
            result += len(nums) - right
            window_count[nums[left]] -= 1
            if window_count[nums[left]] == 0:
                del window_count[nums[left]]
            left += 1
    return result