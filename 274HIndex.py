'''
274. H-Index
Medium
Topics Array, Sorting, Counting, Sort
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
'''
def hIndex(citations):
    citations.sort()
    citationslen = len(citations)
    i = 0
    while i < citationslen and citations[citationslen-i-1]>i:
        i += 1
    return i
# time complexity: O(logn)
# space complexity: O(1)
print(hIndex([3,0,6,1,5]))
print(hIndex([1,3,1]))
def hIndex2(citations):
    citations.sort():
    n = len(citations)
    for i in range(0, len(citations)):
        if citations[i] >= n - i:
            return n - i
    return 0
# time complexity: o(logn)
# space complexity: o(1)
