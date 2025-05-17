'''
1832 Check if the Sentence is Pangram
Easy
Topics - HashTable, String
A pangram is a sentence where every letter of the English alphabet appears at least once. Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
'''
def checkIfPangram(sentence):
    pangramlist = [False for i in range(0, 26)]
    for i in range(0, len(sentence)):
        letterindex = ord(sentence[i]) - ord('a')
        if pangramlist[letterindex] == False:
            pangramlist[letterindex] = True
    for i in range(0, len(pangramlist)):
        if pangramlist[i] == False:
            return False
    return True
    # time complexity: o(n)
    # space complexity: o(1)
sentence = 'thequickbrownfoxjumpsoverthelazydog'
print(checkIfPangram(sentence))
sentence = 'leetcode'
print(checkIfPangram(sentence))