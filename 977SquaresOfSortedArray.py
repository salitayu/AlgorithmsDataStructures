def squaresOfSortedArray(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = len(nums) - 1
    for i in range(n - 1, i - 1, -1):
        if abs(nums[left]) < abs(nums[right]):
            squares = nums[right]
            right -= 1
        else:
            squares = nums[left]
            left += 1
        result[i] = squares * squares
    return result