class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            loc, dom = e.split('@')
            loc = loc.split('+')[0]
            loc = loc.replace('.', '')
            unique.add(f'{loc}@{dom}')
        return len(unique)
