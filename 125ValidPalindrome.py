'''
125. Valid Palindrome
Easy
Topics - Two Pointers, String
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
import re
def isPalindrome(s):
    s = re.sub('[^0-9a-zA-Z]', '', s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
    # time complexity: o(n)
    # space complexity: o(1)
print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
print(isPalindrome(' '))
