'''
Two Sum
Easy
Topics Array HashTable
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
def twoSum(nums, target):
    d = {}
    for i in range(0, len(nums)):
        current = nums[i]
        diff = target - current
        if diff in d:
            return [d[diff], i]
        d[current] = i
    return [-1,-1]
# time complexity: o(n)
# space complexity: o(n)
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))