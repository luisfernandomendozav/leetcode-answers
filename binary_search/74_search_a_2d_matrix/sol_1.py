class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1) - First we need to understand that this is a simple binary
        # search problem, because we are going to treat each row as an
        # individual binary search problem.

        # 2) - We want to iterate through each row, so we pop each row
        # and store it in the row var.

        # 3) - Once we have the row variable filled, we apply binary search.
        
        while len(matrix) > 0:
            row = matrix.pop()
            l,r = 0, len(row) - 1
            while l <= r:
                m = l + ((r-l)//2)
                if row[m] < target:
                    l = m + 1
                elif row[m] > target:
                    r = m - 1
                else:
                    return True
        return False
