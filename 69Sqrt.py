'''
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Constraints:
0 <= x <= 231 - 1
Topics: Math Binary Search
'''
def mySqrt(x):
    if x < 2:
        return x
    left = 0
    right = x // 2
    while left <= right:
        mid = left + (right - left) // 2
        temp = sqrt * sqrt
        if temp == x:
            return mid
        elif temp < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
# time complexity: o(logn)
# space complexity: o(1)
print(mySqrt(4))
print(mySqrt(8))