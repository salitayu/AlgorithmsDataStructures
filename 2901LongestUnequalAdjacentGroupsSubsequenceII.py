'''
longest unequal adjacent groups subsequence ii
you are given string array words, array group, both arrays length n
hamming distance between two strings of equal length is the number of positions at which the correspoding characters are different
you need to select the longest subsequence from an array of indices [0, 1, ..., n - 1] such that the subsequence denoted as [i0, i1, ..., ik-1] having length k,
the following holds:
for adjacent indices in the subsequence, their corresponding groups are unequal, i.e., group[ij] != group[ij+1] for j where 0 < j + 1 < k
words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
return string array containing words corresponding to the indices (in order) in the selected subsequence. return any of them if there are multiple answers
strings in words may be unequal in length
words=['bab', 'dab', 'cab']
groups = [1, 2, 2]
output = ['bab', 'cab']
[0, 2]
'''
class Solution:
    def hammingDistance(self, a, b):
        return sum(1 for x, y in zip(a, b) if x != y)
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        lis = [1] * n
        parent = [-1] * n
        lis_len, lis_end = 1, 0
        for i in range(n):
            for j in range(i+1, n):
                if (
                    groups[i] != groups[j]
                    and len(words[i]) == len(words[j])
                    and self.hammingDistance(words[i], words[j]) == 1
                    and lis[i] + 1 > lis[j]
                ):
                    lis[j] = lis[i] + 1
                    parent[j] = i
                    if lis[j] > lis_len:
                        lis_len = lis[j]
                        lis_end = j
        ans = []
        curr = lis_end
        while curr != -1:
            ans.append(words[curr])
            curr = parent[curr]
        return ans[::-1]