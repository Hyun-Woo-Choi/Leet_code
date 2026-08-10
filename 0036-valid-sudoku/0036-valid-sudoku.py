class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):

                current = board[i][j]

                if current == ".":
                    continue
                
                row_key = (i, current)
                col_key = (current, j)
                box_key = ( i // 3, j // 3, current)


                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True 
        