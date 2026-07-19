class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)

        for index in range(length - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            start, end = index + 1, length - 1
            target = 0 - nums[index]
            while start < end:
                temp = nums[start] + nums[end]
                if temp < target:
                    start += 1
                elif temp > target:
                    end -= 1
                else:
                    result.append([nums[index], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
        return result

