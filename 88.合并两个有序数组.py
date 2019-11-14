class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_nums1 = len(nums1) - 1
        len_nums2 = len(nums2) - 1

        while m - 1 < len_nums1:
            nums1.pop(len_nums1)
            len_nums1 -= 1
        while n - 1 < len_nums2:
            nums2.pop(len_nums2)
            len_nums2 -= 1
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:len(nums1)] = nums2[:]
        nums1.sort()