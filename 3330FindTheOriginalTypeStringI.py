def possibleStringCount(word):
    n = len(word)
    answer = 1
    for i in range(1, n):
        if word[i-1] == word[i]:
            answer += 1
    return answer
# time O(n) # space O(1)