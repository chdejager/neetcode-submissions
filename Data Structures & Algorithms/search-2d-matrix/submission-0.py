class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search for rows then binary search within each row
        bottom = 0
        top = len(matrix) - 1

        while bottom <= top:
            row = (top + bottom) // 2

            if  target < matrix[row][0]:
                top  = row - 1
            elif target > matrix[row][-1]:
                bottom  = row + 1
            else:
                left = 0
                right = len(matrix[row]) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if matrix[row][mid] > target:
                        right = mid - 1
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        return True

                return False

        return False




