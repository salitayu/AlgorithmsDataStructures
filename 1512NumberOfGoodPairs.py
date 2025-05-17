'''
1512. Number of Good Pairs
Easy
Topics - Array Hash Table Math Counting
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
from collections import defaultdict
def numIdenticalPairs(nums):
    counts = defaultdict(int)
    result = 0
    for i in range(0, len(nums)):
        current = nums[i]
        result += counts[current]
        counts[current] += 1
    return result
    # time complexity: o(n)
    # space complexity: o(n)
print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))