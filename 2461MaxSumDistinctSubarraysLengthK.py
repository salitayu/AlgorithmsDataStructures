# array hashtable sliding window
def maximumSubarraySum(nums, k):
    left = 0
    right = 0
    maximum = 0
    visited = set()
    total = 0
    while right < len(nums):
        while nums[right] in visited:
            total -= nums[left]
            visited.remove(nums[left])
            left += 1
        total += nums[right]
        visited.add(nums[right])
        if (right - left + 1) == k:
            maximum = max(maximum, total)
            total -= nums[left]
            visited.remove(nums[left])
            left += 1
        right += 1
    return maximum