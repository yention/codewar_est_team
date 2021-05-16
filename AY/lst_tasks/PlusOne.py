# https://leetcode.com/problems/plus-one/submissions/
'''
    Given a non-empty array of decimal digits representing
    a non-negative integer, increment one to the integer.
    The digits are stored such that the most significant
    digit is at the head of the list, and each element
    in the array contains a single digit.
    You may assume the integer does not contain any
    leading zero, except the number 0 itself.
'''


def plusOne(digits: list[int]) -> list[int]:
    plus = 1
    ind = len(digits)-1
    while plus == 1 and ind >= 0:
        if digits[ind] + plus > 9 and ind != 0:
            digits[ind] = 0
            plus = 1
            ind -= 1
        elif digits[ind] + plus > 9 and ind == 0:
            digits[ind] = 0
            digits.insert(0,1)
            plus = 0
            ind -= 1
        else:
            digits[ind] += plus
            plus = 0
            ind -= 1
    return digits



if __name__ == '__main__':
    ls = [0,0,1]
    print(plusOne(ls))
    # 9,9 -> 1,0,0
