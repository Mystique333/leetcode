class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind1, ind2 = None, None
        for i in range(len(nums)):

            for j in range(len(nums)-1, i, -1):
                if nums[i] + nums[j] == target:
                    ind1, ind2 = i, j
                    break
            if ind1 is not None:
                break
        return [ind1, ind2]
                    
