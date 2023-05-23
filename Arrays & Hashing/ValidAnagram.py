class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = list(s)
        for c in t:
            try:
                hash.remove(c)
            except:
                return False
        return len(hash) == 0