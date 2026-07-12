class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        index = 0
        for n in nums:
            num = target - n
            if map.get(num, None) is None:
                map[n] = index
            else:
                return [map.get(num), index]
            index += 1