# https://leetcode.com/problems/longest-common-prefix/
'''
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
'''


def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) <= 0 or '' in strs:
        if len(strs) > 0:
            frame = min((word for word in strs), key=len)
            while True:
                for w in strs:
                    while w.startswith(frame) != True:
                        frame = frame[:-1]
                    continue
                return frame
        else:
            return ''




if __name__ == '__main__':
    st = ["", 'fo','for']
    print(longestCommonPrefix(st))
