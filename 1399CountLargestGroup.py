def countLargestGroup(n):
    hashmap = collections.Counter()
    for i in range(1, n + 1):
        key = sum([int(x) for x in str(i)])
        hashmap[key] += 1
    maxValue = max(hashmap.values())
    count = sum(1 for v in hashmap.values() if v == maxValue)
    return count
    # time o(logn)
    # space o(logn)