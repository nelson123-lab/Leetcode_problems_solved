class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        return nums1.sort()

"""
Assigning the values of nums2 into nums1 after the elements in the nums1.
"""
