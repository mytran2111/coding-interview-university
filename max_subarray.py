def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        current_sum = nums[0]
        max_sum = current_sum
        
        for idx in range(1, len(nums)):
            current_sum = max(nums[idx], current_sum + nums[idx])
            max_sum = max(max_sum, current_sum)
            
        return max_sum
