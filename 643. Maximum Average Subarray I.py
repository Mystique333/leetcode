class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = None
        cur = 0
        cnt = 0

        for i in range(len(nums)):
            cur +=nums[i]
            cnt +=1

            if cnt == k:
                ans = cur / k
                summ = ans
            if cnt > k:
                cur -= nums[i-k]
                ans = cur / k
                summ = max(summ, ans)
        return summ
