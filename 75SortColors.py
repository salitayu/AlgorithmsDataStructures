"""
75. Sort Colors Medium Topics Array, Two Pointers, Sorting
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
def sortColors(nums):
    left = 0
    right = len(nums) - 1
    pivot = 1
    mid = 0
    while mid <= right:
        if nums[mid] > pivot:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        elif nums[mid] < pivot:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        else:
            mid += 1
    return nums
print(sortColors([2,0,1]))
print(sortColors([2,0,2,1,1,0]))
# time complexity: o(n)
# space complexity: o(1)