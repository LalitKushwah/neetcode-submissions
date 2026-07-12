class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for ch in s:
            if map.get(ch, None) is None:
                map[ch] = 1
            else:
                map[ch] += 1
        for c in t:
            if map.get(c) is None:
                return False
            else:
                map[c] -= 1
        return all(v == 0 for v in map.values())

