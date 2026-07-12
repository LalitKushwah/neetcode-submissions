class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        for sub_array in matrix:
            result = self.binary_search(sub_array, target)
            if result == True:
                return result
        return result

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + int((high - low)/2)
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return True
        return False
