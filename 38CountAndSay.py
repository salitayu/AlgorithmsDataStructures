def countAndSay(n):
    current_string = "1"
    for _ in range(n - 1):
        next_string = ""
        j = 0
        k = 0
        while j < len(current_string):
            while (k < len(current_string) and current_string[k] == current_string[j]):
                k += 1
            next_string += str(k - j) + current_string[j]
            j = k
        current_string = next_string
    return current_string
# time complexity: o(4^n/3)
# space complexity: o(4^n/3)
import re
def countAndSay1(n):
    s = "1"
    for _ in range(n - 1):
        # m.group(0) is the entire match, m.group(1) is its first digit
        # (.) group containing single character that could be anything
        # \\1 is a backreference to whatever matches in group 1, the pattern matched in parenthesis
        # group 1 is the only group (.).
        # * this qualifier followed by the group reference \\1, indicates that we would like to see
        # the group repeat itself 0 or more times
        s = re.sub(r"(.)\\1*", lambda m: str(len(m.group(0))) + m.group(1), s)
    return s