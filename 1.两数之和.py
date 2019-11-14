class Solution:
    def twoSum(self, nums, target) :
        a=len(nums)
        i=0
        while i<len(nums):
            b=i+1
            while b<len(nums):
                if target==nums[i]+nums[b]:
                    return [i,b]
                else:
                    b+=1
            i+=1