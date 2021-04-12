# https://leetcode.com/problems/valid-palindrome/

'''
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
'''
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # x = ' '.join([str(elem) for elem in (re.findall("[a-zA-Z0-9]", s.lower()))])
        # x = ' '.join([str(elem) for elem in x])
        return True if ' '.join([str(elem) for elem in (re.findall("[a-zA-Z0-9]", s.lower()))]) == ' '.join([str(elem) for elem in (re.findall("[a-zA-Z0-9]", s.lower()))])[::-1] else False


if __name__ == '__main__':
    s = ' '
    print(Solution.isPalindrome(0, s))