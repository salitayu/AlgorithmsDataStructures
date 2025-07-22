def makeFancyString(s):
    if len(s) < 3:
        return s
    s = list(s)
    j = 2
    for i in range(2, len(s)):
        if s[i] != s[j-1] or s[i] != s[j-2]:
            s[j] = s[i]
            j += 1
    return ''.join(s[:j])