'''
You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.
Return all possible synonymous sentences sorted lexicographically.

Example 1:

Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
1 <= si.length, ti.length <= 10
si != ti
text consists of at most 10 words.
All the pairs of synonyms are unique.
The words of text are separated by single spaces.
Array
Hash Table
String
Backtracking
Union Find
'''
import collections
import itertools
def generateSentences(synonyms, text):
    uf = {}
    def union(x, y):
        uf[find(y)]=find(x)
    def find(x):
        uf.setdefault(x,x)
        if uf[x]!=x:
            uf[x] = find(uf[x])
        return uf[x]
    for a,b in synonyms:
        union(a,b)
    d = collections.defaultdict(set)
    for a, b in synonyms:
        root=find(a)
        d[root] |= set([a,b])
    txt = text.split()
    res = []
    for t in txt:
        if t not in uf:
            res.append([t])
        else:
            r = find(t)
            res.append(list(d[r]))
    fin_res = [' '.join(sentence) for sentence in itertools.product(*res)]
    return sorted(fin_res)
print(generateSentences([["happy","joy"],["sad","sorrow"],["joy","cheerful"]], "I am happy today but was sad yesterday"))