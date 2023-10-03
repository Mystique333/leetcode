class Solution:
    def removeDuplicates(self, s: str) -> str:
        # d = ''
        # flag = False
        # while True:
        #     for i in range(len(s)-1):
        #         if flag is True:
        #             flag = False
        #             continue
        #         if i == len(s)-2:
        #             d += s[i+1]
        #         if s[i] != s[i+1]:
        #             d += s[i]
        #         else:
        #             flag = True
        #             continue
        #     if s == d:
        #         break
        #     s = d
        #     d = ''
        # return d
        stack = []
        ans = ''
        for st in s:
            if len(stack) != 0 and st == stack[-1]:
                stack.pop()
            else:
                stack.append(st)
        for elem in stack:
            ans += elem
        return ans
