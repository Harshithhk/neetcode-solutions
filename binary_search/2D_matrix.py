class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_count = len(matrix)
        col_count = len(matrix[0])
        top = 0
        bot = rows_count - 1

        while top <= bot:
            row_idx = (top + bot) // 2
            row = matrix[row_idx]

            if target < row[0]:
                bot = row_idx - 1
            elif target > row[-1]:
                top = row_idx + 1
            else:
                break
        if not (top <= bot):
            return False

        print(top, bot)
        row_idx = (top + bot) // 2
        row = matrix[row_idx]

        l = 0
        r = col_count - 1

        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
            else:
                return True

        return False
