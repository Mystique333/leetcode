class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = '', ''
        for i in range(len(s)):
            print(s1)
            if s[i] == '#':
                s1 = s1[:-1]
            else:
                s1 += s[i]
        for i in range(len(t)):
            print(t1)
            if t[i] == '#':
                t1 = t1[:-1]
            else:
                t1 += t[i]
        if t1 == s1:
            return True
        else:
            return False
