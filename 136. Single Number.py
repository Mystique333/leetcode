class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for num in set_nums:
            quantity = nums.count(num)
            if quantity == 1:
                return num
