class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            num = numbers[i]
            temp = target - num
            if map.get(temp, None) is not None:
                return [map.get(temp), i+1]
            else:
                map[num] = i+1