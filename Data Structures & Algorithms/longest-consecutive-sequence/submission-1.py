class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print(nums_set)
        global_max_seq = 0
        for num in nums_set:
            max_seq = 0
            if (num-1) not in nums_set:
                max_seq += 1
                curr = num
                while (curr + 1) in nums_set:
                    curr = curr + 1
                    max_seq += 1
                global_max_seq = max(global_max_seq, max_seq)

        return global_max_seq
