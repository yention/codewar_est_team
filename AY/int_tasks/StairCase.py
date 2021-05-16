# https://leetcode.com/problems/climbing-stairs/
"""
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


def climbStairs(n: int) -> int:
    if n >= 3:
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        for i in range(2, len(arr)):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n - 3] + arr[n - 2]
    elif n == 1 or n == 2:
        return n


if __name__ == '__main__':
    n = 3
    print(climbStairs(n))
