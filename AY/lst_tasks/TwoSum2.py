# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
    Given an array of integers numbers that is already sorted in asc order,
    find two numbers such that they add up to a specific target number.
    Return the indices of the two numbers (1-indexed) as an integer
    array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
    You may assume that each input would have exactly one
    solution and you may not use the same element twice.
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        if (numbers[i] + numbers[j]) == target:
            return [i + 1, j + 1]
        elif (numbers[i] + numbers[j]) < target:
            i += 1
        else:
            j -= 1


if __name__ == '__main__':
    ls = [-1,0,1, 5,7,9]
    trg = -1
    print(f'result = {twoSum(ls, trg)}')

