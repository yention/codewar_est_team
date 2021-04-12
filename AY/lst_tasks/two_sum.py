# https://leetcode.com/problems/two-sum/
'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        st = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    st.add(i)
                    st.add(j)
        return list(st)

if __name__ == '__main__':
    l= [3,3]
    target= 6
    res = Solution.twoSum(0,l,target)
    print(res)