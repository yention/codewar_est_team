# https://leetcode.com/problems/valid-palindrome/
'''
    Given a string s, determine if it is a palindrome,
    considering only alphanumeric characters and ignoring cases.

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
'''
import re


def isPalindrome(s: str) -> bool:
    return re.findall("[a-zA-Z0-9]", s.lower()) == re.findall("[a-zA-Z0-9]", s.lower())[::-1]

if __name__ == '__main__':
    st = "1A man, a plan, a canal: Panama1"
    print(isPalindrome(st))
