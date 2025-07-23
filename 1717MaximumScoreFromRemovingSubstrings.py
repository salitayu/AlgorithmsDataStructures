def maximumGain(s, x, y):
    # you are given a string s and two integers x and y
    # you can perform two types of operations any number of times:
    # remove substrings "ab" and gain x points
    # for example, when removing "ab" from "cabxbae" it becomes "cxbae"
    # remove substring "ba" and gain y points
    # remove "ba" from "cabxbae" to become "cabxe"
    # return the maximum points you can gain after applying the above operations on s.
    # ensure 'ab' always has higher points than 'ba'
    if x < y:
        s = s[::-1]
        x, y = y, x
    a_count, b_count, total_points = 0, 0, 0
    for i in range(len(s)):
        if s[i] == 'a':
            a_count += 1
        elif s[i] == 'b':
            if a_count > 0:
                # can form 'ab', remove it and add points
                a_count -= 1
                total_points += x
            else:
                b_count += 1
        else:
            # non 'a' or 'b' character encountered
            # calculate points for any remaining 'ba' pairs
            total_points += min(b_count, a_count) * y
            # reset counters for next segment
            a_count, b_count = 0
    # calculate points for any remaining "ba" pairs at the end
    total_points += min(b_count, a_count) * y
    return total_points
    # time o(n)
    # space o(1)