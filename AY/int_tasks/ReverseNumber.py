# https://leetcode.com/problems/reverse-integer/
'''
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit
    integer range [-231, 231 - 1], then return 0.
'''


class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if x >= 0 else int(str(x)[0] + str(x).strip('0')[-1:0:-1])
        return int(x) if (-(2**31) <= x <=(2**31) -1) else 0

if __name__ == '__main__':
    x = 2147483647
    print(Solution.reverse(0,x))