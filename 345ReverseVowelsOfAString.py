'''
345 Reverse Vowels of a String
Easy
Topics - Two Pointers, String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper cases, more than once.
'''
def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    left = 0
    right = len(s) - 1
    s = list(s)
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        else:
            left += 1
    return ''.join(s)
    # time complexity: o(n)
    # space complexity: o(n)
print(reverseVowels('IceCreAm'))
print(reverseVowels('leetcode'))