import collections
def numRabbits(answers):
    count = collections.Counter(answers)
    return sum(-v % (k+1) + v for k, v in count.iteritems())
    # time complexity: o(n)
    # space complexity: o(n)
def numRabbits1(answers):
    """
    :type answers: List[int]
    :rtype: int
    """
    total = 0
    d = {}
    for i in answers:
        if i in d:
            d[i] += 1
        else:
            d[i] = 0
            total += i + 1
        if d[i] == i:
            del d[i]
    return total
    # time complexity: o(n)
    # space complexity: o(n)