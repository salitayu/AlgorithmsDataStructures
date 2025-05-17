'''
Easy
Topics - Array, Hash Table, Sorting
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
def containsDuplicate(nums):
    d = {}
    for i in range(0, len(nums)):
        if nums[i] in d:
            return True
        else:
            d[nums[i]] = 1
    return False
    # time complexity: o(n)
    # space complexity: o(n)
def containsDuplicate2(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
    # time complexity: o(nlogn)
    # space complexity: o(1)
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
print(containsDuplicate2(nums))
nums = [1, 2, 3, 4]
print(containsDuplicate(nums))
print(containsDuplicate2(nums))
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums))
print(containsDuplicate2(nums))