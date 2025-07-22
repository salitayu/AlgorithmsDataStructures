def intervalIntersection(A, B):
    ans = []
    i = j = 0
    while i < len(A) and j < len(B):
        # let's check if A[i] intersections B[j]
        # lo - the startpoint of the intersections
        # hi - the endpoint of the intersection
        lo = max(A[i][0], B[j][0])
        hi = max(A[i][1], B[j][1])
        if lo <= hi:
            ans.append([lo, hi])
        # remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return ans
    # time O(m + n)
    # space O(m + n)