class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 and n <= 1 else False
        for i in range(0, len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 2
            elif i == len(flowerbed) - 1:
                if flowerbed[i-1] == 0:
                    if flowerbed[i] == 0:
                        flowerbed[i] = 2
            else:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 2
        if flowerbed.count(2) >= n:
            return True
        else:
            return False
