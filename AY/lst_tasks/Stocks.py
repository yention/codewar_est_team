# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
    You are given an array prices where prices[i] is the price of a
    given stock on the ith day.
    Find the maximum profit you can achieve.
    You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions simultaneously
    (i.e., you must sell the stock before you buy again).

    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
    engaging multiple transactions at the same time. You must sell before buying again.
'''
from typing import List


def maxProfit(prices) -> int:
    abs_min = prices[0]
    total = 0
    buy = 0
    for p in prices:
        if p < abs_min:
            abs_min = p
        elif abs_min < p:
            total += p - abs_min
            abs_min = p

    return total




if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))