class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_general = 0
        for elem in nums:
            count = 0
            while elem:
                elem = elem // 10
                count += 1
            if count % 2 == 0:
                count_general +=1
                    
        return count_general
