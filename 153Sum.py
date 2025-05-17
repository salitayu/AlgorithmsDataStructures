def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i-1] != nums[i]:
            twoSumII(nums, i, res)
    return res
def twoSumII(nums, i, res):
    lo = i + 1
    hi = len(nums) - 1
    while lo < hi:
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
def threeSumClosest(nums, target):
    diff = float('inf')
    nums.sort()
    for i in range(0, len(nums)):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            temp = nums[i] + nums[low] + nums[high]
            if abs(target - temp) < abs(diff):
                diff = target - temp
            if temp < target:
                low += 1
            else:
                high -= 1
            if diff == 0:
                break
    return target - diff
def threeSumSmaller(nums, target):
    nums.sort()
    if len(nums) < 3:
        return 0
    result = 0
    for i in range(0, len(nums)):
        left = i
        middle = i + 1
        right = len(nums) - 1
        while middle < right:
            temp = nums[left] + nums[middle] + nums[right]
            if temp < target:
                result += right - middle
                middle += 1
            else:
                right -= 1
    return result