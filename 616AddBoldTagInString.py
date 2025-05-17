'''
616. Add Bold Tag in String Medium Topics Array, Hash Table, String, Trie, String Matching
You are given a string s and an array of strings words.
You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words.
If two substrings overlap, you should wrap them together with only one pair of closed bold tag.
If two substrings wrapped by bold tags are consecutive, you should combine them.
Return s after adding the bold tags.
'''
def addBoldTag(s, words):
    n = len(s)
    start = 0
    isbold = [False] * n
    result = ''
    for word in words:
        start = s.find(word)
        while start != -1:
            for i in range(start, start + len(word)):
                isbold[i] = True
            start = s.find(word, start + 1)
    for i in range(n):
        if isbold[i] and (i == 0 or not isbold[i-1]):
            result += '<b>'
        result += s[i]
        if isbold[i] and (i == n - 1 or not isbold[i+1]):
            result += '</b>'
    return ''.join(result)
    # time complexity: O(m⋅(n ^ 2 ⋅k−n⋅k ^ 2))
    # space complexity: o(n)
print(addBoldTag('abcxyz123', words=['abc', '123']))