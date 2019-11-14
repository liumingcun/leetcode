class Solution:
    def removeElement(self, nums, val) :
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return(len(nums))




# 双指针法
class Solution:
    def removeElement(self, nums, val) :
        i = 0
        j = 0
        ex = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j