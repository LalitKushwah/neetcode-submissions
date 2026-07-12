from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:            
            trasformed_sorted = "".join(sorted(s))
            map[trasformed_sorted].append(s)
        result = map.values()
        return list(result)

    

