class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:            
            trasformed_sorted = "".join(sorted(s))
            if map.get(trasformed_sorted, None) is not None:
                temp = map[trasformed_sorted]
                temp.append(s)
                map[trasformed_sorted] = temp
            else:
                map[trasformed_sorted] = [s]
        result = map.values()
        return list(result)

    

