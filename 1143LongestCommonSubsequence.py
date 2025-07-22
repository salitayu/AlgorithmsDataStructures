def longestCommonSubsequence(text1, text2):
    x = len(text1)
    y = len(text2)
    values = [[None] * (y + 1) for i in range(x + 1)]
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                values[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                values[i][j] = values[i- 1][j - 1] + 1
            else:
                values[i][j] = max(values[i-1][j], values[i][j - 1])
    return values[x][y]
    # time o(n^2)
    # space o(n)