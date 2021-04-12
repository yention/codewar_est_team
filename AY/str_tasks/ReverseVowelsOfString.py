# https://leetcode.com/problems/reverse-vowels-of-a-string/
'''
    Given a string s, reverse only all the vowels in the string and return it.
    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
    Example 1:
    Input: s = "hello"
    Output: "holle"
    Example 2:
    Input: s = "leetcode"
    Output: "leotcede"
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u']
        res = []
        vowels_lst = []
        for i in range(len(s)):
            if s[i].lower() in v:
                vowels_lst.append(s[i])
        for i in range(len(s)):
            if s[i].lower() in v:
                res.append(vowels_lst.pop())
            else:
                res.append(s[i])
        print(''.join(el for el in res))
        return ''.join(el for el in res)

if __name__ == '__main__':
    s = 'ao'
    Solution.reverseVowels(0,s)
