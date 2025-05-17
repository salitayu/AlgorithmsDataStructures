'''
Given an integer array nums sorted in non decreasing order, remove the duplicates in place such that each uniquee element appears only once
The relative order of the elements should be kept the same.
Return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elmeents of nums are not important as well as the size of nums.
Return k.
'''
def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[k] = nums[i]
            k += 1
    return k
# time o(n)
# space o(1)
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,1,2,2,3,3,4]))
