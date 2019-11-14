class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] < target and nums[i+1] >= target:
                return i+1
            else:
                i += 1