#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, amount):
    """
    How many of these type of coins can I get with my money?
        I'll take a lot. How much money am I left with?
        And how many coins are in my pocket?
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
