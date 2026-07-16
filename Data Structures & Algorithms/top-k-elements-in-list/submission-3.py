class Solution:
    def custom_fn(self, tup):
        key, value = tup
        return value

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for n in nums:
            if map.get(n, None) is None:
                map[n] = 1
            else:
                map[n] += 1
        list = sorted(map.items(),key=self.custom_fn, reverse=True)
        for i in range(k):
            key,value = list[i]
            result.append(key)
        return result
