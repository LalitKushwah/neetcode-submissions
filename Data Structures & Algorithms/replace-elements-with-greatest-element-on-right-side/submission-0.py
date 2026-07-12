class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = len(arr) - 1
        max_so_far = arr[idx]
        while idx >= 0:
            temp = arr[idx]
            arr[idx] = max_so_far
            max_so_far = max(temp, max_so_far)
            idx -= 1
        arr[len(arr)-1] = -1
        return arr

        
            