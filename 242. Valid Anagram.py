class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for st in s:
            if s.count(st) != t.count(st):
                return False
        for st in t:
            if s.count(st) != t.count(st):
                return False
        return True
        
