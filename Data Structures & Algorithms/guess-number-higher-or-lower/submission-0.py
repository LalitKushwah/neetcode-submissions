# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n
        
        num = None
        while num is not 0:
            mid = low + int((high - low)/2)
            num  = guess(mid)
            if num == -1:
                high = mid - 1
            elif num == 1:
                low = mid + 1
        return mid
