# https://leetcode.com/problems/implement-strstr/
'''
    Return the index of the first occurrence of needle
    in haystack, or -1 if needle is not part of haystack.
    Clarification:
    What should we return when needle is an empty string?
    This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when
    needle is an empty string. This is consistent to C's
    strstr() and Java's indexOf().

    Input: haystack = "hello", needle = "ll"
    Output: 2
    Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
    Example 3:

    Input: haystack = "", needle = ""
    Output: 0
'''


def strStr(haystack: str, needle: str) -> int:
    return 0 if needle == '' else -1 if needle not in haystack else haystack.index(needle)

if __name__ == '__main__':
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack= haystack, needle= needle))