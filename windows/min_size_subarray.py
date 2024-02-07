def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    i = 0
    current_sum = 0
    window_size = 0

    # find min window size
    # while current_sum < target keep adding to right
    while i < len(nums) and current_sum < target:
        current_sum += nums[i]
        if current_sum >= target:
            window_size = i + 1
        i += 1
    i = 0
    if window_size <= 1:
        return window_size
    # once window current_sum >= target record min_window size
    # shift left once
    # print('----------------------------')
    # print(target, nums)
    while  i + window_size < len(nums) or current_sum - nums[i] >= target:
        # print(current_sum, nums[i:i+window_size])
        if current_sum - nums[i] >= target:
            window_size -= 1
            current_sum -= nums[i]
            if window_size == 1:
                break
        else:
            current_sum -= nums[i]
            current_sum += nums[i+window_size]
        i += 1
    # print(window_size)
    return window_size
