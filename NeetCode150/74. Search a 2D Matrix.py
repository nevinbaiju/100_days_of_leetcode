class Solution:
    def binary_search(self, arr, target):
        l = 0
        r = len(arr)

        while(l < r):
            # print(arr[l:r], l, r)
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            elif target < arr[mid]:
                r = mid
            else:
                l = mid+1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix)

        while(len(matrix[l_row:r_row]) > 1):
            mid = (l_row + r_row)//2
            comp_arr = matrix[mid]
            if (target>= comp_arr[0]) and (target <= comp_arr[-1]):
                l_row = mid
                r_row = mid+1
            elif (target < comp_arr[0]):
                r_row = mid
            else:
                l_row = mid+1
                
        return l_row < len(matrix) and self.binary_search(matrix[l_row], target)
