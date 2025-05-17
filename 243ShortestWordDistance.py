'''
243. Shortest Word Distance
Easy
Topics - Array, String
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
Constraints:
2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
'''
import sys
def shortestDistance(wordsDict, word1, word2):
    word1index = -1
    word2index = -1
    shortestdistance = sys.maxsize
    for i in range(0, len(wordsDict)):
        current = wordsDict[i]
        if current == word1:
            word1index = i
        if current == word2:
            word2index = i
        if word1index != -1 and word2index != -1:
            shortestdistance = min(abs(word2index - word1index), shortestdistance)
    return shortestdistance
    # time complexity: o(n)
    # space complexity: o(1)
print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))