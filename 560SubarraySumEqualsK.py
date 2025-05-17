def subarraySum(nums, k):
    d = {0: 1}
    currentSum = 0
    count = 0
    for i in nums:
        currentSum += i
        diff = currentSum - k
        count += d.setdefault(diff, 0)
        d[currentSum] = d.setdefault(currentSum, 0) + 1
    return count
    # time complexity: o(n)
    # space complexity: o(n)
    