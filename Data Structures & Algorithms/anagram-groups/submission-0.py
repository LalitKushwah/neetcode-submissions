class Solution:

    def prepare_hash_map(self, s):
        local_hash_map = {}
        for ch in s:
            if local_hash_map.get(ch, None) is not None:
                local_hash_map[ch] += 1
            else:
                local_hash_map[ch] = 1
        return local_hash_map


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        exclude_indexes = []
        result_group = []
        for i,s in enumerate(strs):
            local_result = []
            if i not in exclude_indexes:
                local_result.append(s)
                local_hash_map = self.prepare_hash_map(s)
                for j in range(i+1, len(strs)):
                    hash_map = self.prepare_hash_map(strs[j])
                    if local_hash_map == hash_map:
                        local_result.append(strs[j])
                        exclude_indexes.append(j)
            if local_result:
                result_group.append(local_result)
        return result_group
    

