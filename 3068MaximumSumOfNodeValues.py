def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)
    def maxSumOfNodes(self, index, isEven, nums, k, memo):
        if index == len(nums):
            return 0 if isEven == 1 else -float("inf")
        if memo[index][isEven] != -1:
            return memo[index][isEven]
        # no operation performed on the element
        noXorDone = nums[index] + self.maxSumOfNodes(index + 1, isEven, nums, k, memo)
        # XOR operation is performed on the element
        xorDone = (nums[index] ^ k) + self.maxSumOfNodes(
            index + 1, isEven ^ 1, nums, k, memo
        )
        # memoize and return the result
        memo[index][isEven] = max(xorDone, noXorDone)
        return memo[index][isEven]
    def maximumValueSum(self, nums, k, edges):
        memo = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)
    # time O(n)
    # space O(n)