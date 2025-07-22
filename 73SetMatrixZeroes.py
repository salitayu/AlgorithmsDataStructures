def setZeroes(matrix):
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()
    # mark rows and columsn that are made to be zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    # iterate over array once again and use rows and cols sets, update elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0