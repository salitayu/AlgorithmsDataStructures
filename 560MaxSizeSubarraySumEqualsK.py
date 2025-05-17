'''
325 Maximum Size Subarray Sum Equals k
int array nums and int k, return max length of subarray that sums to k
if there is not one, return 0 instead
nums = [1, -1, 5, -2, 3], k = 3
output = 4
[1, -1, 5, -2] sums to 3 and is the longest
array hashtable prefix sum
'''
def maxSubArrayLen(nums, k):
    prefix_sum = 0
    longest_subarray = 0
    indices = {}
    for i, num in enumerate(nums):
        prefix_sum += num
        # check if all the numbers seen so far sum to k
        if prefix_sum == k:
            longest_subarray = i + 1
        # if any subarray seen so far sums to k, update the length of the longest subarray
        if prefix_sum - k in indices:
            longest_subarray = max(longest_subarray, i - indices[prefix_sum - k])
        # only add the current prefix_sum index pair to the map if prefix_sum is not already in the map
        if prefix_sum not in indices:
            indices[prefix_sum] = i
    return longest_subarray
    # time complexity: o(n)
    # space complexity: o(n)