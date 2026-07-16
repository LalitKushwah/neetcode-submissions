class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for n in nums:
            if map.get(n, None) is None:
                map[n] = 1
            else:
                map[n] += 1
        list = sorted(map.items(),key=lambda item:item[1], reverse=True)
        for i in range(k):
            key,value = list[i]
            result.append(key)
        return result
