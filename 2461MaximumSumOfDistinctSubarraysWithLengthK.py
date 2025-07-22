def maximumSubarraySum(nums, k):
    begin = 0
    end = 0
    numToIndex = {}
    result = 0
    currentSum = 0
    while end < len(nums):
        current = nums[end]
        lastOccurence = numToIndex.get(current, -1)
        while begin <= lastOccurence or end - begin + 1 > k:
            currentSum -= nums[begin]
            begin += 1
        numToIndex[current] = end
        currentSum += nums[end]
        if end - begin + 1 == k:
            result = max(result, currentSum)
        end += 1
    return result
    # time: o(n)
    # space: o(n)