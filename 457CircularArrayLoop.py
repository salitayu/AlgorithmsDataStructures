def circularArrayLoop(nums):
    size = len(nums)
    # iterate through each index of the array 'nums'
    for i in range(size):
        # set slow and fast pointer at current index value
        slow = fast = i
        # set true in 'forward' if element in positive, set false otherwise
        forward = nums[i] > 0
        while True:
            # move slow pointer to one step
            slow = next_step(slow, nums[slow], size)
            # if cycle is not possible, break the loop and start from next element
            if is_not_cycle(nums, forward, slow):
                break
            # first move of fast pointer
            fast = next_step(fast, nums[fast], size)
            # if cycle is not possible, break the loop and start from next element
            if is_not_cycle(nums, forward, fast):
                break
            # second move of fast pointer
            fast = next_step(fast, nums[fast], size)
            # if cycle is not possible, break loop and start from next element
            if is_not_cycle(nums, forward, fast):
                break
            # at any point, if fast and slow pointers meet each other,
            # it indicate that loop has been found, return True
            if slow == fast:
                return True