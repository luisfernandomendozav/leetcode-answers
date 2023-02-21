class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1) - We are going to traverse all the board with two for loops.

        # 2) - We are going to use a dictionary with default set as values.

        # 3) - If we have a '.' then we are going to skip that use case.

        # 4) - We are going to check if that item is already added to rows, to cols or to square.

        # 5) - We now that the item board[r][c] belongs to the row 'r' and to column 'c'.

        # 6) - Thats why we check if the item is added to rows[r] or cols[c].

        # 7) - For the squares dictionary, we have a tuple as a key, but this tuple goes to 1 to 3, because we
        # are taking (0,0), (0,1), (0,2), (0,3) ... (2,0), (2,1), (2,2) => 
        #                                           (0//3, 0//3), (0//3,1//3)...(2//3, 2//3) => 
        #                                           (0,0)
        # So all the values above maps to (0,0) i.e the first 3x3 sub square, then for example the value (3,1) will map 
        # to the subsquare  (1, 0) and so on we have 9 subsquares from (0,0) to (2,2).

        # 8) - Then the squares hashMap will look something like squares = {(0,0): {'1', '3'}, (0,1): {'7'}...}

        # 9) - Then if board[r][c] is already on rows[r], cols[c] or squares[(r//3,c//3)] then is not a valid
        # sudoku and we return False.

        # 10) - If thats not the case we add the value to the set

        # 11) - If we finish traversing the array then we return True.


        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True