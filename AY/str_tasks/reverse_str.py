# https://leetcode.com/problems/reverse-string/

'''
    Write a function that reverses a string. The input string is given as an array of characters s.
    Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
'''


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)

if __name__ == '__main__':
    ls = ["h","e","l","l","o"]
    Solution.reverseString(0,ls)
