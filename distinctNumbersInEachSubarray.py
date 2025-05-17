def distinctNumbers(nums, k):
    len_nums = len(nums)
    answer = [0] * (len_nums - k + 1)
    freq = {}
    for num in nums[:k]:
        freq[num] = freq.get(num, 0) + 1
    answer[0] = len(freq)
    for pos in range(k, len_nums):
        left = nums[pos - k]
        freq[left] -= 1
        if freq[left] == 0:
            del freq[left]        
        right = nums[pos]
        freq[right] = freq.get(right, 0) + 1
        answer[pos - k + 1] = len(freq)
    return answer
