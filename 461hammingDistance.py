def hammingDistance(x, y):
    temp = x ^ y
    result = []
    while temp > 0:
        result.append(temp % 2)
        temp = temp // 2
    return result.count(1)
    