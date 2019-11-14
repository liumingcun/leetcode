class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num = 0
        init = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] == init:
                num += 1
                i += 1
            else:
                num -= 1
                i += 1
            if num == 0:
                init = nums[i]
        return init

