class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1,1]]
        if numRows < 3:
            return dp[:numRows]
        
        for i in range(numRows-2):
            new_row = [1]
            for j in range(1, len(dp[-1])):
                new_row.append(dp[-1][j] + dp[-1][j-1])
            new_row += [1]
            dp.append(new_row)
        return dp
