class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Initiate a list of set of rows
        # 2. Initiate a list of set of columns
        # 3. Initiate a list of set of boxes (optional)

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        # 4. Traverse each element of sudoku board, retrieving the
        # values in the grid, and checking if they already appears in
        # the corresponding set of rows, columns or boxes

        for i in range(9): # Loop for each row
            for j in range(9): # Loop for each column
                el = board[i][j]

                # If el is "." (empty), ignore
                if el == ".":
                    continue

                # 4.1. Check if exists in row set, and return False if positive
                if el in rows[i]:
                    return False
                else:
                    rows[i].add(el)

                # 4.2. Check if exists in columns set, and return False if positive
                if el in columns[j]:
                    return False
                else:
                    columns[j].add(el)

                # 4.3. Check if exists in box set, and return False if positive
                # Here we use modulus operator to address a range to the same box
                # e.g. rows[0:3] & columns[0:3] is the same box
                if el in box[(i // 3) * 3 + j // 3]:
                    return False
                else:
                    box[(i // 3) * 3 + j // 3].add(el)


        # 5. If none of restrictions met, is a valid board
        return True 