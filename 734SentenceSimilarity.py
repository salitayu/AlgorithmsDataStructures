from collections import defaultdict
def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False
    d = defaultdict(set)
    for i in similarPairs:
        d[i[0]].add(d[i[1]])
        d[i[1]].add(d[i[0]])
    for i, j in enumerate(sentence1):
        if (sentence[i] == sentence2[i]) or (sentence2[i] in d[sentence1[i]]):
            continue
        else:
            return False
    return True
print(areSentencesSimilar(["great","acting","skills"], ["fine", "drama", "talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))
# time complexity: O((n+k)*m)
# space complexity: O(k*m)