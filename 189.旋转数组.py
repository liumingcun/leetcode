class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        len_nums = len(nums)

        flag = 0
        for i in range(len_nums):
            if (i + k) % len_nums == 0:  # 说明i位置在变换后是列表的头部
                flag = i
                break

        for i in range(flag):
            nums.append(nums[0])
            nums.pop(0)