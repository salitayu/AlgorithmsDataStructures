def numberOfArrays(differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        differences between each pair of consecutive integers of a hidden sequence of length
        n + 1
        the hidden sequence hidden
        differences[i] = hidden[i+1] - hidden[i]
        lower, upper
        differences=[1,-3,4]
        lower=1
        upper=6
        hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 inclusive
        [3,4,1,5] and [4,5,2,6] are possible hidden sequences
        [5,6,3,7] not possible since it contains element greater than 6
        [1,2,3,4] not possibel since the differences are not correct
        return number of possible hidden sequences, no possible sequences return 0
        array prefix sum
        """
        x = 0
        y = 0
        cur = 0
        for d in differences:
            cur += d
            x = min(x, cur)
            y = max(y, cur)
            if y - x > upper - lower:
                return 0
        return (upper - lower) - (y - x) + 1
        # time o(n)
        # space o(1)
differences = [1,-3,4]
lower = 1
upper = 6
print(numberOfArrays(differences,lower,upper))
differences = [3,-4,5,1,-2]
lower = -4
upper = 5
print(numberOfArrays(differences, lower, upper))
