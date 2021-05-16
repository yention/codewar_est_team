# https://leetcode.com/problems/length-of-last-word/

'''
    Given a string s consists of some words separated by spaces, return
    the length of the last word in the string. If the last word does not exist, return 0.
    A word is a maximal substring consisting of non-space characters only.

    Input: s = "Hello World"
    Output: 5
'''


def lengthOfLastWord(s: str) -> int:

    # s = s.split()
    return 0 if not s.split() else len(s.split()[-1])

if __name__ == '__main__':
    s = 'hello world'
    print(lengthOfLastWord(s))