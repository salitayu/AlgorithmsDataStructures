# array hashtable matrix
def isValidSudoku(board):
    N = 9
    # use hash set to record the status
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]
    for r in range(N):
        for c in range(N):
            val = board[r][c]
            # check if position is filled with number
            if val == '.':
                continue
            # check row
            if val in rows[r]:
                return False
            rows[r].add(val)
            # check the column
            if val in cols[c]:
                return False
            cols[c].add(val)
            # check the box
            idx = (r // 3) * 3 + c // 3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)
    return True
    # time o(n^2)
    # space o(n^2)
