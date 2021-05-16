# https://leetcode.com/problems/maximum-subarray/
'''
    Given an integer array nums, find the contiguous
    subarray (containing at least one number) which has
    the largest sum and return its sum.
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums: list[int]) -> int:
    ans = []
    ans.append(nums[0])
    for i in range(1, len(nums)):
        print('now ans', ans)
        print(f'ans[{i-1}] = {ans[i-1]}')
        ans.append(max(nums[i], ans[i - 1] + nums[i]))
    print(ans)
    return max(ans)


if __name__ == '__main__':

    slt = [8,-19,5,-4,20]
    print(maxSubArray(slt))