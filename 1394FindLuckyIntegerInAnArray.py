def findLucky(arr):
    d = {}
    ans = [-1]
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for k, v in d.items():
        if k == v:
            ans.append(k)
    return max(ans)
# time O(n)
# space O(N)
