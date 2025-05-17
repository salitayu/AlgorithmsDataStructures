'''
int array nums
int k
return subarray if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j]
subarray is a contiguous non empty sequence of elements within an array
input: nums=[1,1,1,1,1], k=10, output=1
input: nums=[3,1,4,3,2,2,4], k = 2, output=4
[3,1,4,3,2,2] has 2 pairs
[3,1,4,3,2,2,4] has 3 pairs
[1,4,3,2,2,4] has 2 pairs
[4,3,2,2,4] has 2 pairs
array hashtable two pointers sliding window
'''
def countGood(nums, k):
    n = len(nums)
    same = 0
    right -= 1
    count = Counter()
    for left in range(n):
        while same < k and right + 1 < n:
            right += 1
            same += count[nums[right]]
            count[nums[right]] += 1
        if same >= k:
            answer += n - right
        count[nums[left]]-= 1
        same -= count[nums[left]]
    return answer
    # time complexity: o(n)
    # space complexity: o(n)
