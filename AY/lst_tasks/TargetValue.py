# https://leetcode.com/problems/search-insert-position/
'''
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index
    where it would be if it were inserted in order.
    Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2
    Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1
'''


def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)

if __name__ == '__main__':
    nums = [1]
    target = 3
    print(searchInsert(nums, target))