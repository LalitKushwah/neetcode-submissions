class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if map.get(num, None) is None:
                map[num] = 1
            else:
                return True
        return False

