# https://leetcode.com/problems/valid-parentheses/
'''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Example 1:
    Input: s = "()"
    Output: true
'''


def isValid(s: str) -> bool:
    # parentheses_d = {
    #     ')': '(',
    #     '}':'{',
    #     ']':'['
    # }
    # res = []
    # for el in s:
    #     if el in list(parentheses_d.values()):
    #         res.append(el)
    #     elif el in list(parentheses_d.keys()):
    #         if res and res[-1] == parentheses_d[el]:
    #             res.pop(-1)
    #         else:
    #             return False
    # return not res

    dict_brt = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    res_list = list()
    if len(s) >= 2:
        for i in s:
            if i in dict_brt.values():
                res_list.append(i)
                # print(f'01res_list = {res_list}')
            elif i in dict_brt.keys():
                if len(res_list) > 0 and res_list[-1] == dict_brt[i]:
                    res_list.pop(-1)
                    # print(f'02res_list = {res_list}')
                    continue
                else:
                    return False
    return True if len(s) >= 2 and len(res_list) == 0 else False



if __name__ == '__main__':
    s = ']'
    print(isValid(s))