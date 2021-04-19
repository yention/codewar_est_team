# https://leetcode.com/problems/ransom-note/
'''
    Given an arbitrary ransom note string and another string containing letters
    from all the magazines, write a function that will return true if the ransom
    note can be constructed from the magazines ; otherwise, it will return false.
    Each letter in the magazine string can only be used once in your ransom note.
    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false
    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false
'''


class Solution:
    def canConstruct(self, r: list, m: str) -> bool:
        if m.count(r) or r == '':
            return True
        else:
            r = list(r)
            for el in sorted(list(m)):
                if el in sorted(r):
                    list(m).pop(m.index(el))
                    (r).pop(r.index(el))
            if r == []:
                return True
            else:
                return False





if __name__ == '__main__':
    r = "fd"
    m = ""
    print(Solution.canConstruct(0, r, m))
