class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        s_cnt = 0
        seq = ''
        for symb in t:
            if symb == s[s_cnt]:
                seq += symb
                s_cnt += 1
                if s == seq:
                    return True
            
        return False
