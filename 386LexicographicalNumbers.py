class Solution:
    def lexicalOrder(self, n):
        lexicographical_numbers = []
        # start generating numbers from 1 to 9
        for start in range(1, 10):
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
        return lexicographical_numbers
    def _generate_lexical_numbers(self, current_number, limit, result):
        # if the current number exceeds the limit, stop recursion
        if current_number > limit:
            return
        # add the current number to the result
        result.append(current_number)
        # try to append digits from 0 to 9 to the current number
        for next_number <= limit:
            self._generate_lexical_numbers(next_number, limit, result)
        else:
            break # no need to continue if next_number exceed limit
    # time: o(n)
    # space: o(log10(n))