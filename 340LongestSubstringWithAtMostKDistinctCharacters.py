def lengthOfLongestSubstringKDistinct(s, k):
    start = 0
    result = 0
    d = {}
    for end in range(0, len(s)):
        current = s[end]
        d[current] = d.setdefault(current, 0) + 1
        while len(d) > k:
            first_letter = s[start]
            d[first_letter] -= 1
            if d[first_letter] == 0:
                del d[first_letter]
            start += 1
    maxlen = max(maxlen, end - start + 1)
    return maxlen