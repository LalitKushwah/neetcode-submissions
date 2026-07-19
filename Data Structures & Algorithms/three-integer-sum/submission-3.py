class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorting in-place is slightly faster than sorted(nums)
        result = []
        length = len(nums)
        
        for index in range(length - 2):
            # FIX 1: Skip duplicate values for the 'first' number
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
                    # Found a valid triplet!
                    result.append([nums[index], nums[start], nums[end]])
                    
                    # FIX 2: Skip duplicate values for the 'start' pointer
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    # FIX 3: Skip duplicate values for the 'end' pointer
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                        
                    # Move both pointers inward after finding a match
                    start += 1
                    end -= 1
                    
        return result